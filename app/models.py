from django.db import models


class Customer(models.Model):
    """
    Model Customer
    """
    customer_id = models.BigAutoField(primary_key=True)
    first_name = models.TextField(max_length=255)
    last_name = models.TextField(max_length=255)
    email = models.ForeignKey('Emails', related_name='customer', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'


class OrderStatus(models.Model):
    """
    Model OrderStatus
    """
    status_id = models.BigAutoField(primary_key=True)
    paid = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Order status'
        verbose_name_plural = 'Order status'


class Orders(models.Model):
    """
    Model Orders
    """
    order_id = models.BigAutoField(primary_key=True)
    order_number = models.TextField(max_length=255)
    customer = models.ForeignKey(Customer, related_name='orders', on_delete=models.CASCADE)
    status = models.ForeignKey(OrderStatus, related_name='orders', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    @property
    def products(self):
        products = []
        for prop in self.order_order_items.all():
            if prop.product:
                products.append((prop.product.product_name, prop.product.price))
            else:
                products.append((prop.p.product_name, prop.p.price))
        return products


class Emails(models.Model):
    """
    Model Emails
    """
    email_id = models.BigAutoField(primary_key=True)
    email_address = models.TextField(max_length=255)

    class Meta:
        verbose_name = 'Email'
        verbose_name_plural = 'Emails'


class CustomProduct(models.Model):
    """
    Model CustomProduct
    """
    product_id = models.BigAutoField(primary_key=True)
    product_name = models.TextField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        verbose_name = 'Custom product'
        verbose_name_plural = 'Custom products'


class NonCustomProduct(models.Model):
    """
    Model NonCustomProduct
    """
    p_id = models.BigAutoField(primary_key=True)
    product_name = models.TextField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        verbose_name = 'Non custom product'
        verbose_name_plural = 'Non custom products'


class OrderItems(models.Model):
    """
    Model OrderItems
    """
    order = models.ForeignKey(Orders, related_name='order_order_items', on_delete=models.CASCADE)
    product = models.ForeignKey(CustomProduct, related_name='product_order_item', on_delete=models.CASCADE, blank=True,
                                null=True)
    p = models.ForeignKey(NonCustomProduct, related_name='custom_product_order_item', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Order item'
        verbose_name_plural = 'Order items'


