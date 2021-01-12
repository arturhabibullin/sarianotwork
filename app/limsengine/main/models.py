from django.db import models

# Create your models here.



class Company(models.Model):
    company = models.CharField('Компания', max_length=50, unique=True, db_index=True)
    def __str__(self):
        return self.company
    class Meta:
        verbose_name = 'компания'
        verbose_name_plural = 'компании'

class Product(models.Model):
    products = models.CharField('продукт', max_length=50, unique=True)
    def __str__(self):
        return self.products
    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'

class Category(models.Model):
    categorys = models.CharField('категория', max_length=50, unique=True, db_index=True)
    def __str__(self):
        return self.categorys
    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'



class Sample(models.Model):
    sample = models.SlugField('Образец', unique=True)
    date_production = models.DateField('Дата производства', db_index=True,auto_now=True)
    company = models.ForeignKey(Company,on_delete=models.CASCADE,verbose_name='компания')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True,null=True,verbose_name='продукт')
    category = models.ManyToManyField(Category,related_name='samples',blank=True, verbose_name='категория')
    bb_for_i = models.IntegerField('Б/Б с', blank=True, null=True)
    bb_and_for = models.IntegerField('Б/Б по',blank=True, null=True)
    pallet_for_i = models.IntegerField('паллеты с',blank=True, null=True)
    pallet_and_for = models.IntegerField('паллеты по',blank=True, null=True)
    repeate = models.BooleanField('повтор',blank=False)
    date_reg = models.DateTimeField('Дата анализа',auto_now_add=True)
    comment = models.TextField('комментарий', blank=True)
   
    def __str__(self):
        return self.sample
    
    class Meta:
        verbose_name = 'образец'
        verbose_name_plural = 'образцы'
        
        
        
# # class Bruker(models.Model):
# #     samples = models.ForeignKey(Sample, on_delete=models.CASCADE)
# #     acidity_value = models.FloatField(blank=True, null=True)
# #     protein = models.FloatField(blank=True, null=True)
# #     ash = models.FloatField(blank=True, null=True)
# #     moisture = models.FloatField(blank=True, null=True)
# #     fat = models.FloatField(blank=True, null=True)
# #     date_pub = models.DateTimeField(auto_now=True)

# #     def __str__(self):
# #         return str(self.samples)
# #     class Meta:
# #         verbose_name = 'спектрометр'
# #         verbose_name_plural = 'спектрометр'

class Fat(models.Model):
    samples = models.ForeignKey(Sample, on_delete=models.CASCADE, related_name='fats')
    fat_blank_cup = models.FloatField('масса пустого стакана', blank=True, null=True)
    fat_sample_mass = models.FloatField('масса навески', blank=True, null=True)
    fat_final_cup_mass = models.FloatField('масса стакана i', blank=True, null=True)
    fat = models.FloatField('массовая доля сырого жира', blank=True, null=True)
    date_pub = models.DateTimeField('дата анализа', auto_now=True)
    
    def __str__(self):
        return str(self.samples)

    def save(self, *args, **kwargs):
        if self.fat_blank_cup != None and self.fat_sample_mass != None and self.fat_final_cup_mass != None:
            self.fat = ((self.fat_final_cup_mass - self.fat_blank_cup) / self.fat_sample_mass) * 100
            super(Fat, self).save(*args, **kwargs)
        else:
            super(Fat, self).save(*args, **kwargs)
    class Meta:
        verbose_name = 'жир'
        verbose_name_plural = 'жир'
       
# # class Protein(models.Model):
# #     samples = models.ForeignKey(Sample, on_delete=models.CASCADE)
# #     sample_mass = models.FloatField('масса навески', max_length=5, blank=True, null=True)
# #     titrant_volume = models.FloatField('объем 0.2 М серной кислоты',blank=True, null=True)
# #     protein = models.FloatField('массовая доля сырого протеина',blank=True, null=True,max_length=4,)
# #     date_pub = models.DateTimeField(auto_now=True)
# #     def __str__(self):
# #         return str(self.samples)
     
# #     def save(self, *args, **kwargs):
# #         if self.sample_mass !=None and self.titrant_volume !=None:
# #             self.protein = (self.titrant_volume * 1.75) / self.sample_mass
# #             self.protein = round(self.protein, 2)
# #             super(Protein, self).save(*args, **kwargs)
# #         else:
# #             super(Protein,self).save(*args, **kwargs)
# #     class Meta:
# #         verbose_name = 'Протеин'
# #         verbose_name_plural = 'Протеин'
    
        