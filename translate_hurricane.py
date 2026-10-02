import re

file_path = r'C:\project\ventimaxsolutions\en\Produk\hurricane.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

replacements = {
    r'VENTILATOR TURBIN INDUSTRI BERTENAGA ANGIN': r'WIND DRIVEN VENTILATOR',
    r'Hurricane Turbin Ventilator': r'HURRICANE',
    r'Solusi Penyejuk dan Hemat Energi untuk Pabrik & Gudang Tanpa Listrik': r'Cooler and Energy-Saving Factory & Warehouse Solution Without Electricity.',
    r'Hurricane adalah turbin ventilator atap bertenaga angin dengan diameter terbesar di dunia \(lebih dari satu meter\) yang dirancang untuk memastikan sirkulasi udara berkelanjutan. Sangat tangguh untuk pabrik, gudang, gedung manufaktur, dan berbagai kompleks industri berskala besar.': r'Hurricane is a wind-powered roof ventilator turbine featuring the world\'s largest diameter (exceeding one meter) designed to ensure continuous air circulation. It is suitable for factories, warehouses, buildings, and all types of structures, ranging from minimalist facilities to large-scale industrial plans.',
    
    r'Konsultasi Proyek': r'Project Consultation',
    r'Lihat Spesifikasi & Data': r'View Specifications & Data',
    
    r'Diameter Terbesar di Dunia \(> 1.000 mm\)': r'World\'s Largest Diameter (> 1,000 mm)',
    r'Material Marine Grade Aluminium Tahan Korosi': r'Corrosion-Resistant Marine Grade Aluminum',
    r'Kapasitas Buang 3.267.000 Liter/Jam': r'Exhaust Capacity 3,267,000 Liters/Hour',
    r'15 Tahun Garansi Resmi Ventimax': r'15 Years Official Ventimax Warranty',
    r'Standar Mutu Industri': r'Industrial Quality Standard',
    r'Dirancang untuk beban angin siklonik ekstrem & sertifikasi ketahanan struktural internasional.': r'Designed for extreme cyclonic wind loads & international structural durability certification.',
    
    r'SPESIFIKASI TEKNIS UTAMA': r'MAIN TECHNICAL SPECIFICATIONS',
    r'Ventilator Bertenaga Angin HURRICANE': r'HURRICANE Wind-Driven Ventilator',
    r'Direkayasa dengan presisi aerodinamika tinggi untuk memberikan performa sirkulasi udara masif tanpa konsumsi daya.': r'Engineered with high aerodynamic precision to provide massive air circulation performance without power consumption.',
    
    r'>Aliran Angin<': r'>Airflow<',
    r'3,267,000': r'3,267,000',
    r'>Liter / Jam<': r'>Liters / Hour<',
    r'Kapasitas maksimum aliran udara terukur untuk mengatasi suhu tinggi dan kelembapan ekstrem pada atap gudang atau manufaktur skala besar.': r'Maximum measured airflow capacity to overcome high temperatures and extreme humidity on large-scale warehouse or manufacturing roofs.',
    
    r'>Material Konstruksi<': r'>Construction Material<',
    r'>Aluminium Tahan Korosi<': r'>Corrosion-Resistant Aluminum<',
    r'Diproduksi menggunakan material aluminium kelas kelautan berdaya tahan tinggi terhadap polusi asam, kelembaban garam pesisir, dan oksidasi cuaca tropis.': r'Manufactured using high-durability marine-grade aluminum resistant to acid pollution, coastal salt humidity, and tropical weather oxidation.',
    
    r'>Komitmen Mutu<': r'>Quality Commitment<',
    r'>15 Tahun<': r'>15 Years<',
    r'>Garansi Resmi Ventimax<': r'>Official Ventimax Warranty<',
    r'Jaminan perlindungan menyeluruh untuk durabilitas struktur turbin dan keandalan mekanis bearing tanpa perlu pelumasan rutin.': r'Comprehensive protection guarantee for turbine structure durability and bearing mechanical reliability without routine lubrication.',
    
    r'STUDI FISIK PRODUK': r'PRODUCT PHYSICAL STUDY',
    r'Unit Hurricane Standar Industri': r'Industrial Standard Hurricane Unit',
    r'Visual unit Hurricane memperlihatkan bilah melengkung aerodinamis presisi yang mampu berputar responsif bahkan pada kecepatan angin rendah.': r'The Hurricane unit visual shows precision aerodynamic curved blades capable of rotating responsively even at low wind speeds.',
    
    r'APLIKASI LAPANGAN': r'FIELD APPLICATION',
    r'Instalasi Atap Pabrik Nyata': r'Real Factory Roof Installation',
    r'Integrasi langsung pada kemiringan atap kompleks manufaktur, menjamin ekstraksi udara panas dan uap pekat secara terus menerus.': r'Direct integration on the roof slope of manufacturing complexes, ensuring continuous extraction of hot air and dense steam.',
    
    r'KEUNGGULAN UTAMA': r'KEY ADVANTAGES',
    r'Kinerja Industri Tanpa Kompromi': r'Uncompromising Industrial Performance',
    r'Sistem ventilasi berkinerja tinggi yang mengatasi kendala termal ruang produksi modern secara mandiri dan berkelanjutan.': r'High-performance ventilation system that overcomes thermal constraints of modern production spaces independently and continuously.',
    
    r'>Tanpa Biaya Listrik<': r'>No Electricity Costs<',
    r'100% bertenaga angin dan konveksi termal alami 24/7. Mengurangi beban operasional gedung secara drastis tanpa memerlukan sambungan kabel dan panel kontrol elektrik.': r'100% wind-powered and natural thermal convection 24/7. Drastically reduces building operational load without requiring electrical wiring and control panels.',
    r'Operasional Zero-Watt': r'Zero-Watt Operation',
    
    r'>Diameter Terbesar di Dunia<': r'>World\'s Largest Diameter<',
    r'Dengan ukuran diameter lebih dari satu meter, turbin dirancang khusus untuk membuang volume panas ekstrem pada manufaktur berat, perakitan, dan fasilitas logistik masif.': r'With a diameter size exceeding one meter, the turbine is specifically designed to extract extreme heat volumes in heavy manufacturing, assembly, and massive logistics facilities.',
    
    r'>Tahan Cuaca Ekstrem<': r'>Extreme Weather Resistant<',
    r'Dibangun dengan Marine Grade Aluminium pilihan: anti-karat, anti-bocor, serta minim perawatan bahkan saat terpapar curah hujan tropis monsun dan terpaan angin badai.': r'Built with selected Marine Grade Aluminum: anti-rust, anti-leak, and minimal maintenance even when exposed to monsoon tropical rainfall and storm winds.',
    r'Standar Maritim Internasional': r'International Maritime Standards',
    
    r'EFISIENSI SISTEM': r'SYSTEM EFFICIENCY',
    r'Konsep Sirkulasi Berkelanjutan': r'Continuous Circulation Concept',
    r'Hurricane memanfaatkan gaya apung termal \(stack effect\) di mana udara panas dalam ruangan yang memuai akan bergerak naik dan diekstraksi ke luar oleh bilah turbin yang senantiasa berotasi oleh aliran angin luar.': r'Hurricane utilizes thermal buoyancy (stack effect) where expanding hot indoor air moves up and is extracted outward by turbine blades continuously rotated by external wind flow.',
    r'Mereduksi kelembapan dan pengembunan plafon': r'Reduces humidity and ceiling condensation',
    r'Mencegah akumulasi gas polutan dan debu industri': r'Prevents accumulation of pollutant gases and industrial dust',
    r'Menciptakan kenyamanan termal pekerja secara merata': r'Creates uniform thermal comfort for workers',
    
    r'>Parameter Desain<': r'>Design Parameter<',
    r'>Nilai Karakteristik<': r'>Characteristic Value<',
    r'>Kategori Sistem<': r'>System Category<',
    r'>Turbin Ventilator Atap Alami \(Wind-Driven\)<': r'>Natural Roof Ventilator Turbine (Wind-Driven)<',
    r'>Diameter Tenggorokan \(Throat\)<': r'>Throat Diameter<',
    r'>Laju Buang Udara \(Maksimum\)<': r'>Air Extraction Rate (Maximum)<',
    r'>Paduan Logam \(Alloy\)<': r'>Metal Alloy<',
    r'>Kompatibilitas Struktur Atap<': r'>Roof Structure Compatibility<',
    r'Metal Sheet, Onduline, Beton, Membran, Zincalume': r'Metal Sheet, Onduline, Concrete, Membrane, Zincalume',
    r'>Masa Garansi Resmi<': r'>Official Warranty Period<',
    r'>15 Tahun Resmi PT Venti Max Solutions<': r'>15 Years Official PT Venti Max Solutions<',
    
    r'>Layanan Pengadaan &amp; Pemasangan Nasional<': r'>Service Coverage<',
    r'Optimalkan Fasilitas Pabrik &amp; Pergudangan Anda dengan Hurricane': r'Optimize Your Factory & Warehouse Facilities with Hurricane',
    r'Tim teknis kami siap melakukan survei lokasi dan menghitung kebutuhan sirkulasi udara optimal untuk fasilitas manufaktur maupun pergudangan Anda cuma-cuma.': r'Our technical team is ready to conduct a site survey and calculate the optimal air circulation requirements for your manufacturing or warehousing facility free of charge.',
    r'Jabodetabek, Bali &amp; Seluruh Indonesia': r'Jabodetabek, Bali &amp; All of Indonesia',
    
    r'>WhatsApp Tim Ahli<': r'>WhatsApp Expert Team<',
    r'>Minta Penawaran Resmi<': r'>Request Official Quote<',
    
    r'>Navigasi Halaman<': r'>Page Navigation<',
    r'>Kategori Produk<': r'>Product Categories<',
    r'>Info Kontak<': r'>Contact Info<',
    r'Telepon Kantor:': r'Phone:',
    r'Sirkulasi udara optimal selama 24 jam tanpa biaya listrik dan dilengkapi dengan insulasi termal bergaransi hingga 15 tahun.': r'Optimal air circulation for 24 hours without electricity costs and equipped with thermal insulation with a guarantee of up to 15 years.',
    
    r'Melayani pengadaan dan pemasangan sistem sirkulasi udara di seluruh Indonesia.': r'Serving the procurement and installation of air circulation throughout Indonesia.',
    r'>Beranda<': r'>Home<',
    r'>Tentang Kami<': r'>About Us<',
    r'>Produk<': r'>Our Products<',
    r'>Proyek<': r'>Our Projects<',
    
    # Header tweaks? "DO NOT modify anything inside the <header> tag!"
}

# The prompt says DO NOT modify <header>. So I should only apply replacements after </header>.
header_end = content.find('</header>')
if header_end != -1:
    header_part = content[:header_end+9]
    body_part = content[header_end+9:]
    for k, v in replacements.items():
        body_part = re.sub(k, v, body_part)
    content = header_part + body_part

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
print("Replacements done!")
