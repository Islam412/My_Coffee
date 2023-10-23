from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from products.models import Product


class Order(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now())
    details = models.ManyToManyField(Product,through='OrderDetails')
    is_finished = models.BooleanField()

    def __str__(self):
        return 'User: '+ self.user.username + ',order id: ' + str(self.id)


class OrderDetails(models.Model):
    product = models.ForeignKey(Product,related_name='order_product',on_delete=models.SET_NULL,null=True,blank=True)
    order = models.ForeignKey(Order,related_name='order_detail',on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=6 , decimal_places=2)
    quantity = models.IntegerField()
    
    def __str__(self):
        return 'User: ' + self.order.user.username + ',Product: ' + self.product.name + 'order id: ' + str(self.order.id)
    class Meta:
        ordering = ['-id']