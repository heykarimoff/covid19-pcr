import os

import qrcode
from django.conf import settings
from django.http import FileResponse
from django.views import generic
from PIL import Image, ImageDraw, ImageFont

from .models import Person


class PeopleDetailView(generic.DetailView):
    slug_field = "guid"
    template_name = 'index.html'
    queryset = Person.objects.all()


class PeopleImageView(generic.DetailView):
    slug_field = "guid"
    template_name = 'index.html'
    queryset = Person.objects.all()

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()

        img = Image.open(os.path.join(settings.MEDIA_ROOT, "layer.jpg"), mode='r')
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype(os.path.join(settings.MEDIA_ROOT, "font.ttf"), size=46)
        draw.text((550, 400), self.object.name, (0,0,0), font=font)
        draw.text((550, 505), self.object.identification_id, (0,0,0), font=font)
        draw.text((550, 610), self.object.birthday.strftime("%d-%m-%Y") , (0,0,0), font=font)
        draw.text((550, 715), self.object.nationality, (0,0,0), font=font)
        draw.text((550, 820), self.object.mobile, (0,0,0), font=font)
        draw.text((1670, 505), self.object.collection_time.strftime("%Y-%m-%d          %H:%M:%S"), (0,0,0), font=font)
        draw.text((1670, 610), self.object.result_time.strftime("%Y-%m-%d          %H:%M:%S"), (0,0,0), font=font)
        draw.text((1670, 715), self.object.report_no, (0,0,0), font=font)
        draw.text((1670, 820), self.object.hesn_no, (0,0,0), font=font)
        url = request.build_absolute_uri(self.object.get_absolute_url())
        qr_img = qrcode.make(url, version=7, box_size=10, border=4)
        img.paste(qr_img, (280, 2870))
        img.save(os.path.join(settings.MEDIA_ROOT, f"images/layer-{self.object.guid}.jpg"))
        
        return FileResponse(open(os.path.join(settings.MEDIA_ROOT, f"images/layer-{self.object.guid}.jpg"), 'rb'), content_type='image/jpeg')
