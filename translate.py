import re

def translate_html():
    with open(r'C:\project\ventimaxsolutions\en\Produk\ventigrille.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # Manual replacements for main section
    html = html.replace('Tingkatkan sirkulasi udara dan estetika interior rumah Anda dengan Ventigrille.', "Elevate your home's airflow and interior aesthetics with the Ventigrille")
    html = html.replace('Ventigrille adalah solusi ventilasi premium yang dirancang untuk memadukan sirkulasi udara berkinerja tinggi secara sempurna dengan tampilan arsitektural yang elegan, menjadikannya peningkatan terbaik bagi hunian modern.', 'A premium ventilation, designed to perfectly balance high-performance air circulation with a sleek, architectural look, the Ventigrille is the ultimate upgrade for modern residential.')

    html = html.replace('Kenyamanan Ruangan yang Optimal:', 'Optimized Indoor Comfort:')
    html = html.replace('Kenyamanan Ruangan yang Optimal', 'Optimized Indoor Comfort')
    html = html.replace('Ventigrille secara efisien mengalirkan udara hangat dan pengap dari dalam ruangan menuju ruang atap, sehingga udara tersebut dapat dibuang secara alami maupun mekanis melalui ventilator atap. Mencegah penumpukan panas serta menjaga suasana tetap sejuk.', 'The Ventigrille efficiently channels warm, stagnant indoor air into the roof space, allowing it to be naturally or mechanically expelled by a roof ventilator. This drastically reduces heat build-up and keeps the atmosphere around you cool and fresh.')
    html = html.replace('Ventigrille secara efisien mengalirkan udara hangat dan pengap dari dalam ruangan menuju ruang atap, sehingga udara tersebut dapat dibuang secara alami maupun mekanis melalui ventilator atap. Hal ini secara drastis mengurangi penumpukan panas serta menjaga suasana di sekitar Anda tetap sejuk dan segar.', 'The Ventigrille efficiently channels warm, stagnant indoor air into the roof space, allowing it to be naturally or mechanically expelled by a roof ventilator. This drastically reduces heat build-up and keeps the atmosphere around you cool and fresh.')
    
    html = html.replace('Desain Minimalis dan Ramping:', 'Minimalist, Low-Profile Design:')
    html = html.replace('Desain Minimalis dan Ramping', 'Minimalist, Low-Profile Design')
    html = html.replace('Dirancang agar tidak mencolok secara visual, Ventigrille memiliki desain kisi-kisi (louver) elegan yang terpasang rata dengan permukaan langit-langit atau dinding, menyatu harmonis dengan arsitektur modern.', 'Engineered to be visually unobtrusive, the Ventigrille features an elegant, louvered design that sits flush against your ceiling or wall. Its clean lines allow it to blend seamlessly into any modern architectural style.')
    html = html.replace('Dirancang agar tidak mencolok secara visual, Ventigrille memiliki desain kisi-kisi (louver) elegan yang terpasang rata dengan permukaan langit-langit atau dinding. Garis desainnya yang bersih memungkinkannya menyatu secara harmonis dengan berbagai gaya arsitektur modern.', 'Engineered to be visually unobtrusive, the Ventigrille features an elegant, louvered design that sits flush against your ceiling or wall. Its clean lines allow it to blend seamlessly into any modern architectural style.')

    html = html.replace('Bekerja Dengan Senyap:', 'Whisper-Quiet Operation:')
    html = html.replace('Bekerja Dengan Senyap', 'Whisper-Quiet Operation')
    html = html.replace('Dibuat dengan presisi untuk dinamika aliran udara yang optimal, kisi-kisi ini memastikan distribusi udara yang lancar tanpa suara siulan atau gemeretak yang mengganggu, yang sering ditemukan pada ventilasi standar.', 'Precision-crafted for optimal airflow dynamics, the grille ensures smooth air distribution without the disruptive whistling or rattling often found in standard vents.')
    html = html.replace('Dibuat dengan presisi untuk dinamika aliran udara yang optimal, kisi-kisi ini memastikan distribusi udara yang lancar tanpa suara siulan atau gemeretak yang sering ditemukan pada ventilasi standar.', 'Precision-crafted for optimal airflow dynamics, the grille ensures smooth air distribution without the disruptive whistling or rattling often found in standard vents.')

    html = html.replace('Pilihan Ukuran Beragam &amp; Finishing Premium:', 'Versatile Sizing &amp; Premium Finishes:')
    html = html.replace('Pilihan Ukuran Beragam &amp; Finishing Premium', 'Versatile Sizing &amp; Premium Finishes')
    html = html.replace('Tersedia dalam berbagai dimensi arsitektural (30×30 cm, 15×40 cm, 15×30 cm) dengan opsi finishing powder coating hitam matte klasik dan putih bersih untuk keselarasan interior hunian.', 'To suit various spatial and design requirements, the Ventigrille is available in multiple dimensions, including 30x30, 15x30, and 15x40. It can be customized in classic matte black, crisp white, or luxurious embossed metallic finishes.')
    html = html.replace('Untuk memenuhi berbagai kebutuhan ruang dan desain, Ventigrille tersedia dalam beragam dimensi, termasuk 30x30, 15x30, dan 15x40. Produk ini dapat disesuaikan dengan pilihan finishing: hitam matte klasik, putih bersih.', 'To suit various spatial and design requirements, the Ventigrille is available in multiple dimensions, including 30x30, 15x30, and 15x40. It can be customized in classic matte black, crisp white, or luxurious embossed metallic finishes.')

    html = html.replace('Pemasangan yang Mudah:', 'Effortless Installation:')
    html = html.replace('Pemasangan yang Mudah', 'Effortless Installation')
    html = html.replace('Dilengkapi dengan rangka yang ringan namun kokoh, Ventigrille dirancang untuk pemasangan yang cepat, presisi, dan praktis, baik untuk konstruksi bangunan baru maupun proyek renovasi.', 'Featuring a lightweight yet durable frame, the Ventigrille is designed for quick, hassle-free installation in both brand-new builds and existing home renovations.')
    html = html.replace('Dilengkapi dengan rangka yang ringan namun kokoh, Ventigrille dirancang untuk pemasangan yang cepat dan praktis, baik untuk bangunan baru maupun renovasi rumah yang sudah ada.', 'Featuring a lightweight yet durable frame, the Ventigrille is designed for quick, hassle-free installation in both brand-new builds and existing home renovations.')

    html = html.replace('Fitur &amp; Keunggulan Utama', 'Key Features &amp; Benefits')

    html = html.replace('VentiGrille Kotak Hitam', 'VentiGrille Square Black')
    html = html.replace('VentiGrille Kotak Putih', 'VentiGrille Square White')
    html = html.replace('VentiGrille Persegi Panjang', 'VentiGrille Rectangular Long')
    html = html.replace('VentiGrille Persegi Pendek', 'VentiGrille Rectangular Short')
    html = html.replace('Produk Ventigrille', 'Our Ventigrille Products')

    html = html.replace('Performa. Presisi. VentiGrille.', 'Performance. Precision. VentiGrille.')
    html = html.replace('VentiGrille menghadirkan pengelolaan aliran udara yang unggul dan tetap stylish', 'Ventigrille delivers superior air management without ever compromising on style.')

    html = html.replace('Koleksi\n                Katalog', 'Our Ventigrille Products')

    # Footer translations
    # Find footer tag
    start = html.find('<footer')
    if start != -1:
        end = html.find('</footer>', start) + 9
        footer = html[start:end]
        footer = footer.replace('Cakupan Layanan', 'Service Coverage')
        footer = footer.replace('Jabodetabek, Bali &amp; Seluruh Indonesia', 'Jabodetabek, Bali &amp; All of Indonesia')
        footer = footer.replace('Sirkulasi udara optimal selama 24 jam tanpa biaya listrik dan dilengkapi dengan insulasi termal bergaransi hingga 15 tahun.', 'Optimal air circulation for 24 hours without electricity costs and equipped with thermal insulation with a guarantee of up to 15 years.')
        footer = footer.replace('Info Kontak', 'Contact Info')
        footer = footer.replace('Telepon Kantor', 'Phone')
        footer = footer.replace('Alamat Kantor', 'Our Office')
        footer = footer.replace('Melayani pengadaan dan pemasangan sistem sirkulasi udara di seluruh Indonesia.', 'Serving the procurement and installation of air circulation throughout Indonesia.')
        
        footer = footer.replace('Tentang Kami', 'About Us')
        footer = footer.replace('Produk', 'Our Products')
        footer = footer.replace('Proyek', 'Our Projects')
        footer = footer.replace('Kontak', 'Contact Us')
        footer = footer.replace('Beranda', 'Home')
        
        html = html[:start] + footer + html[end:]

    with open(r'C:\project\ventimaxsolutions\en\Produk\ventigrille.html', 'w', encoding='utf-8') as f:
        f.write(html)
        
if __name__ == "__main__":
    translate_html()
