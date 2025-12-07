from django.db import models


class MaterialCategory(models.Model):
    """
    Раздел материалов: Учебники, Тетради, Презентации, Теория и т.д.
    """
    name = models.CharField("Назва розділу", max_length=255)

    class Meta:
        verbose_name = "Розділ матеріалів"
        verbose_name_plural = "Розділи матеріалів"

    def __str__(self):
        return self.name


class Material(models.Model):
    """
    Конкретный материал: файл + инфа
    """
    title = models.CharField("Назва матеріалу", max_length=255)
    description = models.TextField("Опис", blank=True)

    # Просто строки, чтобы не зависеть от других приложений
    subject = models.CharField("Предмет", max_length=100)
    school_class = models.CharField("Клас", max_length=20)  # напр. "7-А", "9"

    category = models.ForeignKey(
        MaterialCategory,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="materials",
        verbose_name="Розділ"
    )

    file = models.FileField(
        "Файл",
        upload_to="materials/files/",
        blank=True,
        null=True,
        help_text="Завантаж PDF / DOCX / ZIP та інші файли"
    )

    created_at = models.DateTimeField("Створено", auto_now_add=True)

    class Meta:
        verbose_name = "Матеріал"
        verbose_name_plural = "Матеріали"
        ordering = ["-created_at"]

    def __str__(self):
        return self.title
