from django.db import models
from dealers.models import Dealer
from products.models import Product
from django.utils import timezone

class Order(models.Model):
    STATUS_CHOICES = (
        ( 'DRAFT', 'DRAFT'),
        ('CONFIRMED', 'CONFIRMED'),
        ('DELIVERED', 'DELIVERED'),
    )

    order_number = models.CharField(max_length=30, unique=True, blank=True)
    dealer = models.ForeignKey(Dealer, on_delete=models.SET_NULL, null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='DRAFT')
    total_amount = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.order_number:
            today = timezone.now().strftime('%Y%m%d')
            count = Order.objects.filter(
                created_at__date=timezone.now().date()
            ).count() + 1
            self.order_number = f"ORD-{today}-{count:04d}"
        super().save(*args, **kwargs)

    def update_total(self):
        self.total_amount = sum(i.line_total for i in self.items.all())
        self.save()
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    line_total = models.DecimalField(max_digits=12, decimal_places=2)

    def save(self, *args, **kwargs):
        self.line_total = self.quantity * self.unit_price
        super().save(*args, **kwargs)
        self.order.update_total()