### Ana Cevap

**Ana Noktalar:**
- Araştırmalar, Python tabanlı bir loglama sisteminin kimlik avı e-postaları ve kopyalanmış web sayfalarıyla kullanıcı etkileşimlerini izlemek için kullanılabileceğini göstermektedir.
- Sistem, e-posta açma, link tıklamaları ve veri gönderimleri gibi olayları kaydetmek için HTTP sunucusu ve e-posta takibi araçlarını kullanır.
- Uygulama, pytracking gibi kütüphanelerle kolayca gerçekleştirilebilir, ancak hassas verilerin güvenliği için dikkatli olunmalıdır.

**Sistem Kurulumu:**
Python tabanlı bir loglama sistemi kurmak için aşağıdaki adımları izleyebilirsiniz:
- **HTTP Sunucusu:** Kopyalanmış web sayfalarını sunmak ve etkileşimleri kaydetmek için bir HTTP sunucusu kurun. Bu, GET ve POST isteklerini loglayabilir.
- **E-posta Takibi:** pytracking kütüphanesi kullanarak e-postalara izleme pikselleri ve yönlendirme bağlantıları ekleyin. Bu, e-posta açma ve link tıklamalarını izler.
- **Loglama:** Python'un logging modülü ile tüm etkileşimleri bir dosyaya kaydedin, örneğin e-posta açıldığında veya veri gönderildiğinde.

**Örnek Kullanım:**
- HTTP sunucusu, kopyalanmış web sayfalarına erişimleri ve form gönderimlerini kaydeder.
- E-postalar, izleme pikselleri ile gönderilir; bu pikseller açıldığında sunucu loglar.
- Link tıklamaları, yönlendirme bağlantıları üzerinden izlenir ve loglanır.

**Dikkat Edilmesi Gerekenler:**
- Hassas verilerin kaydedilmesi sırasında gizlilik yasalarına uyulmalıdır.
- Sistem, güvenlik testleri veya eğitim amaçlı kullanılmalıdır; gerçek kimlik avı saldırıları yasalara aykırıdır.

---

### Detaylı Rapor

Bu rapor, kullanıcıların kimlik avı e-postaları ve kopyalanmış web sayfalarıyla etkileşimlerini izlemek için Python tabanlı bir loglama sisteminin uygulanmasını detaylı bir şekilde ele alır. Sistem, e-posta açma, link tıklamaları ve veri gönderimleri gibi olayları kaydetmek üzere tasarlanmıştır. Aşağıda, sistemin bileşenleri, uygulanabilirliği ve dikkat edilmesi gereken noktalar açıklanmıştır.

#### **Giriş ve Arka Plan**
Kimlik avı e-postaları ve kopyalanmış web sayfaları, siber güvenlik testleri ve kullanıcı farkındalık eğitimlerinde sıkça kullanılan araçlardır. Bu tür etkileşimleri izlemek, kullanıcı davranışlarını analiz etmek ve güvenlik açıklarını tespit etmek için önemlidir. Python, bu tür bir sistemin uygulanması için güçlü ve esnek bir programlama dili sunar. Araştırmalar, Python'un logging modülü, http.server modülü ve pytracking gibi kütüphanelerle bu tür bir sistemin kolayca kurulabileceğini göstermektedir.

#### **Sistem Bileşenleri ve İşlevsellik**

##### **1. HTTP Sunucusu Kurulumu**
HTTP sunucusu, kopyalanmış web sayfalarını sunmak ve kullanıcı etkileşimlerini kaydetmek için merkezi bir bileşendir. Bu sunucu, aşağıdaki yolları (paths) işler:

- **/track/open/<encoded_data>**: E-posta açma takibi için izleme pikseli (tracking pixel) sunar ve açma olayını kaydeder. Bu, e-postanın açıldığında sunucuya bir GET isteği gönderen 1x1 piksel görüntüsü ile gerçekleştirilir.
- **/track/click/<encoded_data>**: Link tıklamaları için yönlendirme bağlantısını (redirect link) işler. Tıklama olayını kaydeder ve ardından gerçek URL'ye yönlendirir.
- **/cloned_page/***: Kopyalanmış web sayfalarını sunar ve bu sayfalara yapılan GET ve POST isteklerini kaydeder. Özellikle, form gönderimleri (POST istekleri) veri gönderimlerini loglar.

Örnek bir HTTP sunucusu, Python'un `http.server` modülü kullanılarak şu şekilde kurulabilir:

```python
import http.server
import socketserver
import logging
import pytracking

# Logging kurulumu
logging.basicConfig(filename='interaction_log.txt', level=logging.INFO, format='%(asctime)s - %(message)s')

class MyHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path.startswith('/track/open/'):
            encoded_data = self.path[len('/track/open/'):]
            result = pytracking.get_open_tracking_result(encoded_data)
            logging.info(f'Email opened with metadata: {result.metadata}')
            self.send_response(200)
            self.send_header('Content-type', 'image/png')
            self.end_headers()
            self.wfile.write(pytracking.get_open_tracking_pixel())
        elif self.path.startswith('/track/click/'):
            encoded_data = self.path[len('/track/click/'):]
            result = pytracking.get_click_tracking_result(encoded_data)
            logging.info(f'Link clicked with metadata: {result.metadata}, to URL: {result.tracked_url}')
            self.send_response(302)
            self.send_header('Location', result.tracked_url)
            self.end_headers()
        elif self.path.startswith('/cloned_page/'):
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'<html><body>Cloned page</body></html>')
            logging.info(f'Accessed cloned page: {self.path} from {self.client_address[0]}')
        else:
            self.send_response(404)
            self.end_headers()

    def do_POST(self):
        if self.path.startswith('/cloned_page/'):
            length = int(self.headers.get('content-length', 0))
            body = self.rfile.read(length)
            logging.info(f'Data submitted to {self.path} from {self.client_address[0]}: {body}')
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'<html><body>Thank you for submitting</body></html>')
        else:
            self.send_response(404)
            self.end_headers()

PORT = 8080
with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
    print(f"Serving at port {PORT}")
    httpd.serve_forever()
```

Bu kod, kopyalanmış web sayfalarına erişimleri, e-posta açma ve link tıklamalarını loglar. POST istekleri, veri gönderimlerini kaydetmek için kullanılır.

##### **2. E-posta Gönderme ve Takip**
E-postalar, HTML içeriği ile gönderilir ve `pytracking` kütüphanesi kullanılarak izleme pikselleri ve yönlendirme bağlantıları eklenir. `pytracking`, e-posta açma ve link tıklamalarını izlemek için şu özellikleri sunar:

- **Izleme Pikseli (Open Tracking):** E-postaya eklenen 1x1 şeffaf bir piksel, e-posta açıldığında sunucuya bir GET isteği gönderir. Bu, açma olayını kaydetmek için kullanılır.
- **Yönlendirme Bağlantıları (Click Tracking):** E-postadaki tüm linkler, tıklama olayını kaydetmek ve ardından gerçek URL'ye yönlendirmek için yeniden yazılır.

Örnek bir e-posta gönderme işlemi şu şekilde gerçekleştirilebilir:

```python
import smtplib
from email.mime.text import MIMEText
import pytracking

config = pytracking.Configuration(
    base_open_tracking_url='http://myserver.com/track/open/',
    base_click_tracking_url='http://myserver.com/track/click/',
)

html_email = """
<html>
<body>
<p>Hello, please visit <a href="[invalid url, do not cite] link</a></p>
</body>
</html>
"""

adapted_html = pytracking.adapt_html(html_email, extra_metadata={'email_id': 123}, configuration=config)

msg = MIMEText(adapted_html, 'html')
msg['Subject'] = 'Phishing Email'
msg['From'] = 'sender@example.com'
msg['To'] = 'recipient@example.com'

with smtplib.SMTP('smtp.example.com') as server:
    server.send_message(msg)
```

Bu kod, e-postayı gönderir ve izleme pikselleri ile yönlendirme bağlantılarını ekler. E-posta açıldığında veya link tıklandığında, sunucu bu olayları loglar.

##### **3. Loglama ve Veri Kaydı**
Tüm etkileşimler, Python'un `logging` modülü kullanılarak bir dosyaya kaydedilir. Örneğin:

- E-posta açma: `logging.info(f'Email opened with metadata: {result.metadata}')`
- Link tıklaması: `logging.info(f'Link clicked with metadata: {result.metadata}, to URL: {result.tracked_url}')`
- Web sayfası erişimi: `logging.info(f'Accessed cloned page: {self.path} from {self.client_address[0]}')`
- Veri gönderimi: `logging.info(f'Data submitted to {self.path} from {self.client_address[0]}: {body}')`

Loglar, daha sonra analiz edilmek üzere bir dosyaya yazılır (örneğin, `interaction_log.txt`).

#### **Dikkat Edilmesi Gereken Noktalar**
- **Gizlilik ve Güvenlik:** Hassas verilerin kaydedilmesi sırasında, özellikle form gönderimlerinde, veri gizliliği yasalarına (örneğin, GDPR) uyulmalıdır. POST isteklerinde gelen veriler, yalnızca gerekli bilgiler loglanmalı ve hassas veriler sanitize edilmelidir.
- **Yasal Sınırlar:** Bu sistem, yalnızca güvenlik testleri veya eğitim amaçlı kullanılmalıdır. Gerçek kimlik avı saldırıları, yasalara aykırıdır ve ciddi sonuçlar doğurabilir.
- **Performans:** Büyük ölçekli uygulamalarda, logların bir veritabanına kaydedilmesi veya gerçek zamanlı analiz için yapılandırılması gerekebilir.

#### **Tablo: Sistem Bileşenleri ve İşlevleri**

| **Bileşen**          | **İşlev**                                      | **Örnek Kullanım**                          |
|-----------------------|------------------------------------------------|---------------------------------------------|
| HTTP Sunucusu         | Kopyalanmış sayfaları sunar, istekleri kaydeder | `/cloned_page/*` için GET/POST loglama      |
| Izleme Pikseli        | E-posta açma olayını kaydeder                 | `/track/open/<encoded_data>` üzerinden log  |
| Yönlendirme Bağlantısı| Link tıklamalarını kaydeder, yönlendirir       | `/track/click/<encoded_data>` üzerinden log |
| E-posta Gönderme      | Izleme pikselleri ve bağlantılar ekler         | HTML e-postayı `pytracking` ile modifiye et |

#### **Sonuç**
Bu sistem, kullanıcıların kimlik avı e-postaları ve kopyalanmış web sayfalarıyla etkileşimlerini izlemek için etkili bir yöntem sunar. Python programlama diliyle kolayca uygulanabilir ve güvenlik testleri veya kullanıcı davranışı analizleri için değerli veriler sağlar. Sistem, hem e-posta açma ve link tıklamalarını hem de web sayfası etkileşimlerini kaydederek, kapsamlı bir izleme sağlar.

---

#### **Ana Kaynaklar**
- [Email open and click tracking library](https://github.com/powergo/pytracking)
- [Python Logging Documentation](https://docs.python.org/3/howto/logging.html)
- [Simple HTTP Server for Logging Requests](https://gist.github.com/mdonkers/63e115cc0c79b4f6b8b3a6b797e485c7)
