import re

def update_id_file():
    with open(r'C:\project\ventimaxsolutions\Produk\ventigrille.html', 'r', encoding='utf-8') as f:
        html = f.read()

    html = html.replace('Mencegah penumpukan panas serta menjaga suasana tetap sejuk.', 'Hal ini secara drastis mengurangi penumpukan panas serta menjaga suasana di sekitar Anda tetap sejuk dan segar.')
    html = html.replace('menyatu harmonis dengan arsitektur modern.', 'Garis desainnya yang bersih memungkinkannya menyatu secara harmonis dengan berbagai gaya arsitektur modern.')
    html = html.replace('yang sering ditemukan pada ventilasi standar.', 'yang mengganggu, yang sering ditemukan pada ventilasi standar.')
    html = html.replace('Tersedia dalam berbagai dimensi arsitektural (30×30 cm, 15×40 cm, 15×30 cm) dengan opsi finishing powder coating hitam matte klasik dan putih bersih untuk keselarasan interior hunian.', 'Untuk memenuhi berbagai kebutuhan ruang dan desain, Ventigrille tersedia dalam beragam dimensi, termasuk 30x30, 15x30, dan 15x40. Produk ini dapat disesuaikan dengan pilihan finishing: hitam matte klasik, putih bersih.')
    html = html.replace('untuk pemasangan yang cepat, presisi, dan praktis, baik untuk konstruksi bangunan baru maupun proyek renovasi.', 'untuk pemasangan yang cepat dan praktis, baik untuk bangunan baru maupun renovasi rumah yang sudah ada.')
    
    with open(r'C:\project\ventimaxsolutions\Produk\ventigrille.html', 'w', encoding='utf-8') as f:
        f.write(html)
        
if __name__ == "__main__":
    update_id_file()
