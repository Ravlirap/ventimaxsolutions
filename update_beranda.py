import re
import os

def update_file(file_path, replacements):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Split to keep header safe
    main_start = content.find('<main')
    header_part = content[:main_start]
    main_part = content[main_start:]

    for old, new in replacements:
        main_part = main_part.replace(old, new)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(header_part + main_part)

en_replacements = [
    ('SOLUSI VENTILASI ALAMI', 'NATURAL VENTILATION SOLUTIONS'),
    ('Ruangan Lebih Sejuk.<br>Performa Lebih Baik.', 'Cooler Rooms.<br>Better Performance.'),
    ('Venti Max menghadirkan solusi ventilasi inovatif dan ramah lingkungan yang meningkatkan kenyamanan, menghemat energi, serta menciptakan lingkungan yang lebih baik secara alami.', 'Venti Max provides innovative and eco-friendly ventilation solutions that enhance comfort, save energy, and naturally create better environments.'),
    ('Jelajahi Produk', 'Explore Products'),
    ('Konsultasi Gratis', 'Free Consultation'),
    ('DIDESAIN DI AUSTRALIA', 'DESIGNED IN AUSTRALIA'),
    ('Standar kualitas tinggi untuk lingkungan tropis.', 'High quality standards for tropical environments.'),
    ('TEKNOLOGI TURBIN', 'TURBINE TECHNOLOGY'),
    ('Desain dipatenkan untuk aliran udara maksimal.', 'Patented design for maximum airflow.'),
    ('PERUMAHAN & INDUSTRIAL', 'RESIDENTIAL & INDUSTRIAL'),
    ('Kami memberikan hasil nyata secara signifikan.', 'We deliver significant real results.'),
    ('MASA DEPAN LEBIH SEJUK', 'A COOLER FUTURE'),
    ('Mengurangi panas. Hemat energi secara alami.', 'Reduce heat. Save energy naturally.'),
    ('SEKILAS TENTANG VENTIMAX', 'ABOUT VENTIMAX SOLUTIONS'),
    ('Efisiensi Termal Alami Tanpa Beban Listrik', 'Natural Thermal Efficiency Without Electrical Load'),
    ('Venti Max Solutions adalah perusahaan yang berdedikasi untuk menciptakan ruang hunian dan tempat kerja yang lebih nyaman serta hemat energi. Kami memiliki spesialisasi dalam menyediakan turbin ventilator dan sistem isolasi termal modern yang dirancang untuk mengurangi panas tanpa menggunakan listrik, sehingga mendinginkan ruangan Anda secara alami dan efisien.', 'Venti Max Solutions is a company dedicated to creating more comfortable and energy-efficient living and working spaces. We specialize in providing ventilator turbines and modern thermal insulation systems designed to reduce heat without the use of electricity, cooling your space naturally and efficiently.'),
    ('LAYANAN SPESIALIS', 'SPECIALIST SERVICES'),
    ('Apa yang Kami Tawarkan', 'Our Products'),
    ('Sinergi sirkulasi kinetik alami dan perisai radiasi panas berstandar global.', 'Synergy of natural kinetic circulation and global standard heat radiation shielding.'),
    ('Ventilator Bertenaga Angin Berkinerja Tinggi', 'High-Performance Wind-Driven Ventilator'),
    ('Ventilator bertenaga angin kami berfungsi membuang udara panas dan lembap dari ruang bawah atap (attic), sehingga meningkatkan sirkulasi udara tanpa memerlukan listrik.', 'Our wind-driven ventilator works to exhaust hot, humid air from the attic, thereby improving air circulation without the need for electricity.'),
    ('Performa Aerodinamis', 'Aerodynamic Performance'),
    ('Ventilator Bertenaga Angin', 'Wind Driven Ventilators'),
    ('Ventilator turbin atap yang dirancang untuk menjaga sirkulasi udara tetap berjalan setiap saat pada pabrik, gudang, gedung, dan berbagai jenis bangunan lainnya.', 'Hurricane is a wind-powered roof turbine ventilator designed to keep air circulation running at all times for factories, warehouses, buildings, and all kinds of structures.'),
    ('Ventilator turbin atap yang dirancang untuk menjaga sirkulasi udara tetap berjalan setiap saat.', 'Roof turbine ventilators designed to keep air circulation running at all times.'),
    ('Operasional 24 Jam Nonstop', '24/7 Nonstop Operation'),
    ('Insulasi Termal Modern', 'Modern Thermal Insulation'),
    ('Produk insulasi kami mampu memantulkan panas radiasi dan meningkatkan efisiensi termal bangunan secara keseluruhan, menjadikan ruangan terasa lebih sejuk dan nyaman.', 'Our insulation products are capable of reflecting radiant heat and improving the overall thermal efficiency of the building, making rooms feel cooler and more comfortable.'),
    ('Reflektifitas Radiasi >97%', 'Radiation Reflectivity &gt;97%'),
    ('Produk yang Dirancang untuk Mengurangi Panas Tanpa Listrik.', 'Products Designed to Reduce Heat Without Electricity'),
    ('Venti Max Solutions menyediakan sistem ventilasi turbin tanpa listrik dan insulasi termal yang efisien untuk properti industri, komersial, dan hunian di seluruh Indonesia.', 'Venti Max Solutions provides electricity-free turbine ventilation systems and efficient thermal insulation for industrial, commercial, and residential properties throughout Indonesia.'),
    ('Kapasitas Maks', 'Maximum Airflow Capacity'),
    ('3,267,000 Liter / Jam', '3,267,000 Liters / Hour'),
    ('Material', 'Material'),
    ('Aluminium Korosi Marine', 'Marine Grade Corrosion-Resistant Aluminium'),
    ('Garansi', 'Warranty'),
    ('15 Tahun Resmi', '15 Years'),
    ('Minta Penawaran Hurricane', 'Request Hurricane Quote'),
    ('Insulasi Atap Berbahan Aluminium Foil', 'Aluminum Foil-Based Roof Insulation'),
    ('Venticool adalah insulasi atap berbahan aluminium foil yang dipasang di antara atap dan plafon rumah atau bangunan untuk memantulkan panas agar tidak masuk ke dalam bangunan.', 'Venticool is an aluminum foil-based roof insulation placed between the roof and ceiling of a house/building to repel heat entering the house/building.'),
    ('Daya Pantul > 97%', 'Reflectivity > 97%'),
    ('Daya Pantul', 'High reflectivity'),
    ('Komposisi', 'Composition'),
    ('100% Aluminum Foil Murni', '100% high-quality aluminum foil'),
    ('10 Tahun Garansi', '10 Years'),
    ('SupaVent™ adalah ventilator turbin atap bertenaga angin yang dirancang untuk menjaga sirkulasi udara tetap berjalan setiap saat tanpa menggunakan listrik.', 'SupaVent™ is a wind-powered roof turbine ventilator designed to keep air circulation running at all times without electricity.'),
    ('Tenaga Penggerak', 'Power Source'),
    ('Bertenaga Angin Murni', 'No electricity required: Wind-Powered'),
    ('Material Tahan Korosi', 'Corrosion-resistant material'),
    ('Polikarbonat UV-Stabil', 'Polycarbonate'),
    ('15 Tahun Masa Pakai', '15-Year Service Life'),
    ('Minta Penawaran SupaVent', 'Request SupaVent Quote'),
    ('Minta Penawaran Venticool', 'Request Venticool Quote'),
    ('PRINSIP KERJA TERMAL', 'THERMAL WORKING PRINCIPLE'),
    ('Desain Ventilator Bertenaga Angin', 'Wind-Driven Design Powered'),
    ('Turbin berputar bersama angin untuk menciptakan efek isapan kuat yang membuang udara panas dan pengap dari dalam bangunan, menarik udara sejuk dan segar masuk melalui celah bukaan.', 'The turbine rotates with the wind to create a powerful suction effect that exhausts hot and stale air from the building, drawing in cool and fresh air through openings.'),
    ('Efek Termal Stack', 'Thermal Stack Effect'),
    ('Udara panas secara alami naik ke puncak atap dan langsung ditarik keluar sebelum menembus ruang hunian bawah.', 'Hot air naturally rises to the roof peak and is immediately extracted before penetrating the living space below.'),
    ('Sirkulasi Silang', 'Cross Circulation'),
    ('Angin yang berhembus melintasi turbin menciptakan tekanan negatif, memastikan pergantian udara bersih secara kontinu.', 'Wind blowing across the turbine creates negative pressure, ensuring continuous exchange of clean air.'),
    ('KEUNGGULAN UTAMA', 'KEY ADVANTAGES'),
    ('Mengapa Memilih Ventimax Solutions', 'Why Choose Ventimax Solutions'),
    ('Dirancang untuk kinerja tahan lama, efisiensi maksimal, dan investasi tanpa biaya operasional.', 'Designed for long-lasting performance, maximum efficiency, and zero operational cost investment.'),
    ('Ventilasi Tanpa Listrik', 'Electricity-Free Ventilation'),
    ('Bekerja secara alami memanfaatkan angin dan perbedaan suhu, menghasilkan aliran udara berkelanjutan tanpa biaya energi tambahan.', 'Works naturally with wind and temperature differences, provide continuous airflow without additional energy costs.'),
    ('Biaya Listrik', 'Electricity Cost'),
    ('Rp 0,- / Bulan', 'Rp 0,- / Month'),
    ('Pengendalian Suhu yang Hemat Biaya', 'Cost-Effective Temperature Control'),
    ('Mengurangi ketergantungan pada AC dan sistem pendingin lainnya, sehingga membantu menghemat biaya listrik.', 'Reduces dependence on air conditioning and other cooling systems, helping save on electricity expenses.'),
    ('Beban Pendingin', 'Cooling Load'),
    ('Turun s/d 35%', 'Drops up to 35%'),
    ('Tahan Lama &amp; Tahan Cuaca', 'Durable &amp; Weather Resistant'),
    ('Terbuat dari material antikarat berkualitas tinggi, dirancang untuk tahan terhadap kondisi cuaca ekstrem dan memiliki masa pakai yang panjang.', 'Made from high-quality anti-rust materials, designed to withstand extreme weather conditions and have a long life.'),
    ('Jaminan Pabrik', 'Factory Guarantee'),
    ('Garansi s/d 15 Tahun', 'Up to 15 Years Warranty'),
    ('KLIEN KAMI', 'OUR CLIENTS'),
    ('Klien Kami Yang Telah Menggunakan<br>', 'Our Respective Clients<br>'),
    ('Klien Kami Yang Telah Menggunakan\n              <span class="text-secondary">Produk Ventimax Solutions</span>', 'Our Respective Clients\n              <span class="text-secondary">of Ventimax Solutions Products</span>'),
    ('Dipercaya oleh berbagai industri manufaktur, pergudangan, fasilitas komersial, dan hunian di seluruh Indonesia.', 'Trusted by various manufacturing industries, warehousing, commercial facilities, and homes across Indonesia.'),
    ('GRATIS KONSULTASI', 'FREE CONSULTATION'),
    ('Hitung Potensi Penghematan Anda', 'Calculate Your Savings Potential'),
    ('Dapatkan perhitungan akurat mengenai kebutuhan aliran udara dan isolasi termal untuk area atap bangunan Anda. Ajukan permintaan konsultasi gratis sekarang.', 'Get precise calculations of airflow and thermal insulation requirements for your building\'s roof area. Request a free consultation now.'),
    ('Analisis Beban Panas Bebas Biaya', 'Free Heat Load Analysis'),
    ('Rekomendasi Spesifikasi Tepat Guna', 'Appropriate Specification Recommendation'),
    ('Respon cepat tim teknis kami dalam 1x24 jam kerja', 'Fast response from our technical team within 24 working hours'),
    ('Cakupan Layanan', 'Service Coverage'),
    ('Jabodetabek, Bali &amp; Seluruh Indonesia', 'Jabodetabek, Bali &amp; All of Indonesia'),
    ('Sirkulasi udara optimal selama 24 jam tanpa biaya listrik dan dilengkapi dengan insulasi termal bergaransi hingga 15 tahun.', 'Optimal air circulation for 24 hours without electricity costs and equipped with thermal insulation with a guarantee of up to 15 years.'),
    ('Navigasi Halaman', 'Page Navigation'),
    ('Kategori Produk', 'Product Categories'),
    ('Info Kontak', 'Contact Info'),
    ('Telepon Kantor:', 'Phone:'),
    ('Email:', 'Email:'),
    ('Instagram:', 'Instagram:'),
    ('Website:', 'Website:'),
    ('Melayani pengadaan dan pemasangan sistem sirkulasi udara di seluruh Indonesia.', 'Serving the procurement and installation of air circulation throughout Indonesia.')
]

update_file('C:/project/ventimaxsolutions/en/Beranda.html', en_replacements)

# Apply formatting/exact texts for Indonesian file if any discrepancies exist (usually already matching, but just to be sure)
id_replacements = [
    ('Sekilas Tentang       Ventimax Solutions', 'Sekilas Tentang Ventimax Solutions')
]
update_file('C:/project/ventimaxsolutions/Beranda.html', id_replacements)

print("Replacement complete.")
