from django.db import models

class CompanyInfo(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название компании")
    description = models.TextField(verbose_name="Описание компании")
    logo = models.ImageField(upload_to='company/', verbose_name="Логотип",blank=True, null=True)
    phone = models.CharField(max_length=20, verbose_name="Номер телефона")
    email = models.EmailField(verbose_name="Электронная почта")
    address = models.CharField(max_length=255, verbose_name="Адрес")
    social_links = models.TextField(verbose_name="Ссылки на соцсети", help_text="Укажите ссылки, каждую с новой строки")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Информация о компании"
        verbose_name_plural = "Информация о компании"

class ServiceModel (models.Model):
    service_name = models.CharField(max_length=100, verbose_name="Название услуги")
    description = models.TextField(verbose_name="Описание услуги")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    image = models.ImageField(upload_to='services/', verbose_name="Изображение услуги",blank=True, null=True    )

    def __str__(self):
        return self.service_name

    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"

class Info (models.Model):
    coin = models.CharField(max_length=50, verbose_name="Информация о компании")
    title = models.CharField(max_length=100, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Содержание")
    meaning = models.CharField(max_length=255, verbose_name="Значение")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Сообщение"
        verbose_name_plural = "Сообщении"

# Create your models here.
