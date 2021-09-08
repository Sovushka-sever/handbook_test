from django.db import models


class VersionHandbook(models.Model):
    """
    Модель версии справочника.
    """
    version = models.CharField(
        max_length=50,
        blank=False,
        null=False,
        verbose_name='Версия справочника',
        default='1.0.0'
    )
    start_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата начала действия версии справочника'
    )

    def __str__(self):
        return f'v {self.version}'

    class Meta:
        verbose_name = 'Справочник'
        verbose_name_plural = 'Справочники'
        ordering = ('-version',)


class Handbook(models.Model):
    """
    Модель справочника.
    """
    title = models.CharField(
        unique=True,
        max_length=250,
        verbose_name='Наименование'
    )
    short_title = models.CharField(
        max_length=150,
        verbose_name='Короткое наименование'
    )
    description = models.TextField(
        blank=True,
        verbose_name='Описание'
    )
    version = models.ForeignKey(
        VersionHandbook,
        on_delete=models.PROTECT,
        verbose_name='Версия справочника'
    )
    date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата добавления справочника'
    )

    def __str__(self):
        return f'{self.short_title} - v {self.version}'

    class Meta:
        verbose_name = 'Справочник'
        verbose_name_plural = 'Справочники'
        unique_together = ('title', 'version')
        ordering = ('-date',)


class Element(models.Model):
    """
    Модель элемента справочника.
    """
    handbook = models.ForeignKey(
        Handbook,
        related_name='handbooks',
        on_delete=models.CASCADE,
        verbose_name='Справочник'
    )
    el_code = models.CharField(
        max_length=50,
        blank=False,
        null=False,
        verbose_name='Код элемента'
    )
    el_value = models.CharField(
        max_length=250,
        blank=False,
        null=False,
        verbose_name='Значение элемента'
    )

    def __str__(self):
        return self.el_code

    class Meta:
        verbose_name = 'Элемент справочника'
        verbose_name_plural = 'Элементы справочника'
        ordering = ('-handbook',)
