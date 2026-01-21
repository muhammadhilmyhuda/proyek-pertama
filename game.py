#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
BISIKAN DARI KABUT
Game Petualangan Teks dengan Misteri & Teka-Teki

Tema: Misteri, petualangan, atmofer gelap penuh teka-teki
Cerita: Pemain terbangun di desa terlupakan dengan kabut tebal.
        Ada ritual lama yang mengikat desa ini.
        Setiap pilihan memiliki konsekuensi.

Author: AI Programmer
"""

import random
import time
from typing import Dict, List, Optional

# ============================================================================
# KONFIGURASI GAME
# ============================================================================

class GameState:
    """Menyimpan status pemain dan game"""
    def __init__(self):
        self.hp = 100
        self.inventory: Dict[str, bool] = {
            "kunci_karat": False,
            "catatan_lusuh": False,
            "obor": False,
            "jimat_pelindung": False,
            "pisau_tua": False,
            "artefak_hutan": False,
            "artefak_runtuhan": False,
            "jurnal_ritual": False,
            "artefak_inti": False,
        }
        self.visited_locations: Dict[str, bool] = {
            "desa": False,
            "rumah_tua": False,
            "sumur": False,
            "lonceng": False,
            "hutan": False,
            "reruntuhan": False,
            "gua": False,
            "inti_misteri": False,
        }
        self.completed_puzzles: Dict[str, bool] = {
            "simbol_batu": False,
            "ritual_simbol": False,
            "tulisan_kuno": False,
        }
        self.story_flags: Dict[str, bool] = {
            "ingatan_dimulai": False,
            "tahu_tentang_ritual": False,
            "tahu_nama_di_dinding": False,
            "bertemu_entitas": False,
            "ritual_diperkuat": False,
            "ritual_dihancurkan": False,
            "desa_pertama_kali": False,
            "hutan_pertama_kali": False,
            "reruntuhan_pertama_kali": False,
            "gua_pertama_kali": False,
        }

# ============================================================================
# FUNGSI UTILITAS
# ============================================================================

def clear_screen():
    """Membersihkan layar terminal"""
    print("\n" * 3)

def pause():
    """Memberi jeda sebelum melanjutkan"""
    input("\n[Tekan ENTER untuk melanjutkan...]")
    clear_screen()

def typewriter_effect(text: str, delay: float = 0.02):
    """Efek teks berjalan (typewriter effect)"""
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()

def show_status(game_state: GameState):
    """Menampilkan status pemain"""
    print("=" * 60)
    print(f"❤️  HP: {game_state.hp}/100")
    
    items = [item for item, has in game_state.inventory.items() if has]
    if items:
        print(f"🎒 Inventori: {', '.join(items)}")
    else:
        print(f"🎒 Inventori: (kosong)")
    print("=" * 60)

def get_choice(options: List[str]) -> int:
    """Mendapatkan pilihan dari pemain"""
    while True:
        try:
            for i, option in enumerate(options, 1):
                print(f"{i}. {option}")
            choice = int(input("\nPilihan Anda: "))
            if 1 <= choice <= len(options):
                return choice
            else:
                print("❌ Pilihan tidak valid!")
        except ValueError:
            print("❌ Masukkan angka yang valid!")

def check_inventory_item(game_state: GameState, item: str) -> bool:
    """Mengecek apakah pemain memiliki item tertentu"""
    return game_state.inventory.get(item, False)

def add_item(game_state: GameState, item: str):
    """Menambah item ke inventori"""
    if item in game_state.inventory:
        game_state.inventory[item] = True
        print(f"✅ Anda mendapatkan: {item}")

def remove_item(game_state: GameState, item: str):
    """Menghapus item dari inventori"""
    if item in game_state.inventory:
        game_state.inventory[item] = False

def take_damage(game_state: GameState, damage: int):
    """Memberikan damage ke pemain"""
    game_state.hp -= damage
    print(f"💥 Anda menerima {damage} damage! HP saat ini: {game_state.hp}")

# ============================================================================
# CERITA & DIALOG - PROLOG
# ============================================================================

def prolog(game_state: GameState):
    """Prolog game - pengenalan awal"""
    clear_screen()
    typewriter_effect("=" * 70)
    typewriter_effect("                    BISIKAN DARI KABUT")
    typewriter_effect("=" * 70)
    pause()
    
    clear_screen()
    typewriter_effect("""
Mata Anda terbuka dalam kegelapan.

Kepala panas, ingatan kabur. Anda tidak tahu siapa Anda atau bagaimana 
Anda sampai di sini. Hanya ada kabut—kabut tebal yang menutupi segalanya.

Gradual, penglihatan Anda membaik. Anda melihat rumah-rumah tua, jalan 
yang tersepi. Desa yang hampir ditinggalkan. Langit abu-abu, tidak ada 
matahari, tidak ada burung. Hanya keheningan yang menekan.

Suara bel yang pelan—bel dari menara di kejauhan. Bunyi itu terasa... aneh.
Seolah-olah bel itu memangil Anda.

Seseorang berjalan mendekat dalam kabut. Sosok tua, wajahnya tersembunyi 
dalam bayangan.

TETUA DESA: "Oh... Anda sudah bangun. Kami menunggu Anda..."
""")
    pause()

    clear_screen()
    typewriter_effect("""
TETUA DESA: "Nama Anda... adalah Raven. Anda sudah lama tidur."

Anda mencoba mengingat. Tetapi pikiran Anda kosong. Nama itu terasa asing, 
namun... terasa benar.

ANDA: "Siapa Anda? Di mana saya?"

Tetua tersenyum aneh. Tersenyum tanpa kegembiraan.

TETUA DESA: "Anda ada di rumah, Raven. Di Desa Senja. Tempat di mana 
segala hal berakhir. Tempat di mana kami semua sudah lama menunggu."

Kabut menebal. Udara terasa dingin. Ada sesuatu yang sangat salah 
di tempat ini.
""")
    pause()

# ============================================================================
# BAB 1 - DESA TERLUPAKAN
# ============================================================================

def desa_terlupakan(game_state: GameState) -> Optional[str]:
    """Lokasi utama: Desa Terlupakan - tempat pertama Raven terbangun"""
    game_state.visited_locations["desa"] = True
    
    clear_screen()
    show_status(game_state)
    
    if not game_state.story_flags["desa_pertama_kali"]:
        typewriter_effect("""
Anda memutuskan untuk menjelajahi desa lebih dalam. Rumah-rumah tua 
dengan jendela gelap mengelilingi Anda.

Tetua desa menghampiri Anda dengan senyum aneh yang membuat Anda 
merasa tidak nyaman.

TETUA DESA: "Ah, Raven... Anda ingin belajar lebih banyak tentang 
desa kita yang kecil ini? Baiklah. Ada yang harus Anda ketahui."
""")
        game_state.story_flags["desa_pertama_kali"] = True
        pause()
    
    clear_screen()
    show_status(game_state)
    
    typewriter_effect("""
Anda melihat empat lokasi penting di desa:

• BALAI DESA - tempat penduduk berkumpul
• RUMAH TUA TERKUNCI - mansion gelap di tepi desa
• SUMUR KERING - sumur tua yang terlihat sangat dalam
• MENARA LONCENG - menara yang berbunyi sendiri setiap malam
""")
    
    options = [
        "Pergi ke Balai Desa",
        "Coba membuka Rumah Tua",
        "Lihat ke dalam Sumur Kering",
        "Naik ke Menara Lonceng",
        "Kembali ke Menu Utama"
    ]
    
    choice = get_choice(options)
    
    if choice == 1:
        return balai_desa(game_state)
    elif choice == 2:
        return rumah_tua(game_state)
    elif choice == 3:
        return sumur_kering(game_state)
    elif choice == 4:
        return menara_lonceng(game_state)
    elif choice == 5:
        return None

def balai_desa(game_state: GameState) -> Optional[str]:
    """Balai Desa - bertemu penduduk"""
    clear_screen()
    show_status(game_state)
    
    typewriter_effect("""
Balai Desa adalah bangunan besar dengan arsitektur tua. Pintu masuk 
terbuka. Di dalamnya, beberapa penduduk desa duduk diam.

Mereka semua memandang Anda saat Anda memasuki ruangan. Senyum tipis 
di wajah mereka. Mata mereka... kosong.

TETUA DESA: "Raven... Anda sudah sampai ke sini. Bagus."

PENDUDUK 1: "Ya... dia sudah kembali. Ritual akan segera dimulai."

PENDUDUK 2: "Jangan pergi jauh-jauh, Raven. Kabut itu... dia akan 
membawa Anda kembali ke sini."

Anda merasa ada sesuatu yang sangat salah dengan orang-orang ini. 
Kata-kata mereka penuh makna tersembunyi.

TETUA DESA: "Ada yang ingin Anda ketahui? Atau... ada yang ingin 
Anda lakukan?"
""")
    
    options = [
        "Tanyakan tentang desa dan ritual",
        "Tanyakan siapa diri Anda sebenarnya",
        "Ambil CATATAN LUSUH yang ada di meja",
        "Keluar dari Balai Desa"
    ]
    
    choice = get_choice(options)
    
    if choice == 1:
        clear_screen()
        typewriter_effect("""
ANDA: "Apa yang kalian maksud dengan ritual?"

Tetua tertawa pelan—suara yang membuat bulu kuduk berdiri.

TETUA DESA: "Ritual adalah... cara kami menjaga keseimbangan, Raven. 
Ada sesuatu di bawah desa ini. Sesuatu yang tua. Sesuatu yang lapar. 
Kami telah memberikan apa yang dia inginkan selama berabad-abad."

PENDUDUK 1: "Anda adalah pemberian kami untuk tahun ini, Raven. 
Atau sebenarnya... Anda adalah pemberian dari tahun lalu. Anda 
belum siap saat itu. Tapi sekarang... sekarang saatnya."

Anda merasa nyali Anda hilang. Kedengarannya seperti Anda adalah 
bagian dari rencana mereka.
""")
        game_state.story_flags["tahu_tentang_ritual"] = True
        pause()
        return desa_terlupakan(game_state)
    
    elif choice == 2:
        clear_screen()
        typewriter_effect("""
ANDA: "Siapa saya sebenarnya? Saya tidak bisa mengingat apa pun!"

Tetua terdiam untuk waktu yang lama. Mata mereka melihat melampaui Anda.

TETUA DESA: "Anda adalah... yang terpilih. Nama Anda adalah Raven. 
Anda datang ke desa ini lima tahun lalu. Anda melihat sesuatu yang 
tidak seharusnya Anda lihat. Sesuatu yang gelap. Jadi kami..."

Dia berhenti. Seolah-olah dia mengatakan terlalu banyak.

TETUA DESA: "...kami membuat Anda lupa. Untuk kebaikan Anda. Untuk 
kebaikan semua orang."

Anda mencoba mengingat, tetapi hanya ada kegelapan.
""")
        game_state.story_flags["ingatan_dimulai"] = True
        pause()
        return desa_terlupakan(game_state)
    
    elif choice == 3:
        clear_screen()
        typewriter_effect("""
Anda melihat meja kayu tua di sudut ruangan. Di atasnya tergeletak 
catatan yang rusak, tinta sudah pudar. Anda mengambilnya dengan hati-hati.

TETUA DESA: "Ah... catatan itu. Ambil saja jika Anda mau. Itu hanya 
cerita lama. Cerita tentang orang-orang yang datang sebelum Anda."

Anda baca beberapa baris:

"27 Agustus - Ada yang aneh dengan lonceng itu. Berbunyi lebih keras. 
Semakin banyak kabut."

"2 September - Mereka mengatakan seseorang akan datang. Seseorang untuk 
'menyelamatkan' kita. Saya tidak mengerti."

"15 September - RAHASIA ITU HARUS TETAP TERSEMBUNYI. UNTUK KESELAMATAN 
SEMUA ORANG."

Catatan berikutnya robek dan tidak terbaca.
""")
        add_item(game_state, "catatan_lusuh")
        pause()
        return desa_terlupakan(game_state)
    
    elif choice == 4:
        return desa_terlupakan(game_state)

def rumah_tua(game_state: GameState) -> Optional[str]:
    """Rumah Tua Terkunci - dengan puzzle"""
    clear_screen()
    show_status(game_state)
    
    typewriter_effect("""
Rumah tua di tepi desa ini terlihat lebih tua dari yang lain. 
Pintunya terkunci dengan rantai berkarat. Jendela-jendelanya dipenuhi 
debu tebal.

Anda mendengar suara bisikan di dalam. Suara yang sangat tipis. 
Seolah-olah ruangan itu sendiri yang berbicara.

Jika Anda mendekatkan telinga ke pintu, Anda mendengar:

"...jangan biarkan dia masuk... jangan biarkan dia ingat... 
kabut harus tetap tebal..."

Di depan pintu, ada tiga simbol yang terukir di kayu:

⚫ Bulan (Kegelapan)
⚪ Matahari (Cahaya)
🔺 Segitiga (Keseimbangan)

Ada sebuah slot di samping. Tampaknya ini adalah sebuah teka-teki.
""")
    
    if check_inventory_item(game_state, "kunci_karat"):
        typewriter_effect("\nAnda memiliki KUNCI KARAT. Mungkin bisa digunakan di sini.")
    
    options = [
        "Gunakan KUNCI KARAT (jika punya)",
        "Pilih simbol: Bulan ⚫",
        "Pilih simbol: Matahari ⚪",
        "Pilih simbol: Keseimbangan 🔺",
        "Kembali ke Desa"
    ]
    
    choice = get_choice(options)
    
    if choice == 1:
        if check_inventory_item(game_state, "kunci_karat"):
            clear_screen()
            typewriter_effect("""
Anda memasukkan kunci karat ke dalam slot. Dengan gemeretak, 
pintu terbuka perlahan.

Di dalam, sebuah ruangan gelap dengan rak-rak penuh buku. 
Di tengah ruangan, sebuah meja dengan PETA TERLIPAT yang cukup tua.

Anda mengambil peta. Di dalamnya tergambar wilayah di sekitar desa:
- Hutan Berkabut (barat)
- Reruntuhan Kuno (selatan)
- Gua Terlarang (bawah tanah)

Peta ini akan membantu perjalanan Anda.
""")
            add_item(game_state, "catatan_lusuh")  # Sudah diambil atau tidak
            pause()
            return desa_terlupakan(game_state)
        else:
            clear_screen()
            typewriter_effect("""
Anda tidak memiliki kunci yang tepat. Anda mencoba menutup slot,
tetapi sesuatu yang keras di dalamnya menggigit jari Anda!

Aaah! Anda menarik tangan Anda dengan cepat. Jari Anda berdarah.

Anda menerima 10 damage!
""")
            take_damage(game_state, 10)
            pause()
            return rumah_tua(game_state)
    
    elif choice == 2:
        clear_screen()
        typewriter_effect("""
Anda menekan simbol Bulan. Seketika, terdengar suara yang mengerikan—
seperti ribuan suara meraung sekaligus. Pintu terguncang kuat!

Kabut gelap menyembur keluar dari celah pintu. Anda terpukul mundur!

Anda menerima 15 damage!

Mungkin itu bukan jawaban yang benar...
""")
        take_damage(game_state, 15)
        pause()
        return rumah_tua(game_state)
    
    elif choice == 3:
        clear_screen()
        typewriter_effect("""
Anda menekan simbol Matahari. Hal yang sama terjadi—suara mengerikan 
dan kabut gelap menyembur keluar.

Anda menerima 15 damage!
""")
        take_damage(game_state, 15)
        pause()
        return rumah_tua(game_state)
    
    elif choice == 4:
        clear_screen()
        typewriter_effect("""
Anda menekan simbol Keseimbangan. Hal yang terjadi adalah... 
kedamaian.

Bisikan di dalam rumah berhenti. Pintu terbuka perlahan dengan suara 
yang menenangkan.

Di dalam, sebuah ruangan gelap dengan rak-rak penuh buku berdebu. 
Di tengah ruangan, ada PETA TERLIPAT yang cukup tua, dan sebuah 
KUNCI KARAT kecil di atas meja.

Anda mengambil keduanya.

Peta menunjukkan:
- Hutan Berkabut (barat)
- Reruntuhan Kuno (selatan)
- Gua Terlarang (bawah tanah)
""")
        add_item(game_state, "kunci_karat")
        game_state.completed_puzzles["ritual_simbol"] = True
        pause()
        return desa_terlupakan(game_state)
    
    elif choice == 5:
        return desa_terlupakan(game_state)

def sumur_kering(game_state: GameState) -> Optional[str]:
    """Sumur Kering - dengan item"""
    clear_screen()
    show_status(game_state)
    
    typewriter_effect("""
Sumur ini sangat tua, dindingnya retak. Di dalamnya, gelap sekali. 
Anda membuang batu kecil ke dalamnya. 

Tidak ada suara. Seolah-olah batu itu tidak pernah jatuh. 
Seolah-olah sumur ini tidak memiliki dasar.

Tapi tunggu... di kedalaman yang sangat jauh, ada cahaya aneh. 
Cahaya yang berkilau dengan warna tidak alami.

Anda melihat tali tua yang digulung di tepi sumur. Jika Anda turun...

Atau, di samping sumur, ada sebuah OBOR TUA yang terletak di rumput. 
Obor itu masih bisa digunakan.
""")
    
    options = [
        "Ambil OBOR TUA",
        "Turun ke dalam sumur (beresiko)",
        "Kembali ke Desa"
    ]
    
    choice = get_choice(options)
    
    if choice == 1:
        clear_screen()
        typewriter_effect("""
Anda mengambil obor. Meski terlihat tua, api di ujungnya masih 
menyala dengan cahaya orange yang hangat.

Cahaya ini akan membantu Anda melihat di tempat-tempat gelap.
""")
        add_item(game_state, "obor")
        pause()
        return desa_terlupakan(game_state)
    
    elif choice == 2:
        clear_screen()
        typewriter_effect("""
Anda mengambil tali dan mulai turun ke dalam sumur. Gelap. 
Semakin gelap.

Saat Anda semakin dalam, suara-suara aneh mulai terdengar. 
Bisikan yang berbisik nama Anda. Berkali-kali. Berkali-kali.

RAVEN... RAVEN... RAVEN...

Anda panik dan mulai memanjat ke atas. Dengan tergesa-gesa, 
Anda keluar dari sumur. Jantung Anda berdetak sangat cepat.

Anda menerima 20 damage karena ketakutan dan kelelahan!
""")
        take_damage(game_state, 20)
        pause()
        return desa_terlupakan(game_state)
    
    elif choice == 3:
        return desa_terlupakan(game_state)

def menara_lonceng(game_state: GameState) -> Optional[str]:
    """Menara Lonceng - tempat penting"""
    clear_screen()
    show_status(game_state)
    
    typewriter_effect("""
Menara lonceng tinggi menjulang di atas desa. Setiap langkah Anda ke 
atas, suara lonceng semakin keras. 

Bukan bunyi normal. Bunyi lonceng ini terasa seperti... menangis. 
Seperti peringatan. Seperti doa.

Saat Anda mencapai puncak, Anda melihat lonceng besar yang tergantung. 
Tapi lonceng itu... bergerak sendiri. Tanpa ada angin. Tanpa ada 
yang menyentuhnya.

Setiap kali lonceng berbunyi, Anda merasa ada sesuatu yang 
merespons dari bawah. Dari dalam tanah.

Di bawah lonceng, tergambar simbol ritual yang kompleks. 
Ada banyak tanggal yang terukir di papan kayu tua:

1823, 1856, 1892, 1934, 1973, 2018, 2023

Setiap tanggal dipisahkan dengan tanda silang.
""")
    
    options = [
        "Pelajari simbol ritual (butuh pengetahuan)",
        "Coba hentikan lonceng",
        "Turun dan tinggalkan menara"
    ]
    
    choice = get_choice(options)
    
    if choice == 1:
        clear_screen()
        if game_state.story_flags["tahu_tentang_ritual"]:
            typewriter_effect("""
Anda memahami—tanggal-tanggal ini adalah siklus ritual. Setiap 
50-60 tahun, mereka mengulang ritual. Setiap kali, ada yang 
'dipilih'. 

Dan Anda... Anda adalah yang dipilih kali ini.

Simbol ritual di dasar lonceng adalah lambang 'Penjaga Gerbang'—
makhluk yang dijaga oleh desa ini selama berabad-abad.

Anda merasa ngeri, tetapi juga penasaran. Anda harus tahu lebih 
banyak.
""")
        else:
            typewriter_effect("""
Simbol-simbol ini terlalu kompleks untuk Anda pahami saat ini. 
Anda memerlukan lebih banyak informasi.
""")
        pause()
        return menara_lonceng(game_state)
    
    elif choice == 2:
        clear_screen()
        typewriter_effect("""
Anda mencoba menghentikan lonceng dengan tangan Anda. 

Saat tangan Anda menyentuh lonceng, sejengkal api biru melompat 
dari permukaannya. Anda terlempar mundur!

Anda menerima 25 damage!

Lonceng tidak bisa dihentikan. Ritual ini lebih kuat dari Anda.
""")
        take_damage(game_state, 25)
        pause()
        return menara_lonceng(game_state)
    
    elif choice == 3:
        return desa_terlupakan(game_state)

# ============================================================================
# BAB 2 - HUTAN BERKABUT
# ============================================================================

def hutan_berkabut(game_state: GameState) -> Optional[str]:
    """Lokasi: Hutan Berkabut - penuh misteri"""
    game_state.visited_locations["hutan"] = True
    clear_screen()
    show_status(game_state)
    
    if not game_state.story_flags["hutan_pertama_kali"]:
        typewriter_effect("""
Anda memutuskan meninggalkan desa dan melangkah ke hutan barat. 
Kabut semakin tebal saat Anda menjauh dari desa.

Pohon-pohon tinggi terlihat seperti tulang raksasa yang membusuk. 
Tidak ada bunyi binatang. Tidak ada angin. Hanya keheningan yang 
menakutkan.

Saat Anda berjalan lebih dalam, Anda mendengar suara—suara yang 
memanggil nama Anda. Tetapi itu bukan suara manusia. Itu seperti 
bisikan ribuan bayangan.

BISIKAN: "Raven... kembali... kembali ke sini..."

Peta yang Anda temukan (jika ada) menunjukkan tiga jalur berbeda.
""")
        game_state.story_flags["hutan_pertama_kali"] = True
        pause()
    
    clear_screen()
    show_status(game_state)
    
    typewriter_effect("""
Anda ada di Hutan Berkabut. Jalan bercabang menjadi tiga arah:

1. JALAN BATU TUA - ada simbol-simbol batu di tanah, tapi kabut 
   terlalu tebal untuk dilihat jelas.

2. JALUR RAWA - terdengar suara air, tapi juga suara sesuatu yang 
   bergerak di dalamnya.

3. JALAN RAHASIA - jika Anda memiliki PETA, Anda bisa melihat 
   jalan tersembunyi di sini.
""")
    
    options = []
    options.append("Ikuti Jalan Batu Tua")
    options.append("Masuki Jalur Rawa")
    
    if check_inventory_item(game_state, "catatan_lusuh"):
        options.append("Ikuti Jalan Rahasia (punya peta)")
    
    options.append("Kembali ke Desa")
    
    choice = get_choice(options)
    
    if choice == 1:
        return jalan_batu(game_state)
    elif choice == 2:
        return jalur_rawa(game_state)
    elif choice == 3 and check_inventory_item(game_state, "catatan_lusuh"):
        return jalan_rahasia(game_state)
    elif choice == len(options):
        return None

def jalan_batu(game_state: GameState) -> Optional[str]:
    """Jalan Batu Tua - dengan puzzle simbol"""
    clear_screen()
    show_status(game_state)
    
    typewriter_effect("""
Anda mengikuti jalan batu. Batu-batu ini membentuk pola. Ada simbol 
di setiap batu:

🟠 LINGKARAN - "Awal"
⬛ KOTAK - "Struktur"
🔺 SEGITIGA - "Keseimbangan"
❌ SILANG - "Akhir"

Urutan batu adalah: LINGKARAN - SILANG - KOTAK - SEGITIGA

Tiba-tiba, kabut di sekitar Anda mulai bergerak dengan aneh. 
Bayangan-bayangan mulai terbentuk dari kabut itu. Mereka mengelilingi 
Anda.

BISIKAN: "Selesaikan puzzle... atau kami ambil Anda..."

Anda harus mengurutkan simbol dengan benar. Jika salah, bayangan 
akan menyerang!
""")
    
    options = [
        "Urutan: Lingkaran - Kotak - Segitiga - Silang",
        "Urutan: Lingkaran - Segitiga - Kotak - Silang",
        "Urutan: Silang - Lingkaran - Kotak - Segitiga",
        "Urutan: Lingkaran - Kotak - Silang - Segitiga"
    ]
    
    choice = get_choice(options)
    
    if choice == 2:  # Benar: Awal - Keseimbangan - Struktur - Akhir
        clear_screen()
        typewriter_effect("""
Anda mengurutkan batu dengan benar. Bayangan-bayangan berhenti. 
Mereka meledak menjadi kabut lagi.

Dari depan, cahaya aneh bersinar. Sebuah jalan terbuka, membawa Anda 
ke hutan yang lebih dalam.

Di tanah, ada sebuah JIMAT PELINDUNG yang terlihat kuno. Mungkin 
milik orang yang tersesat di sini sebelumnya.

Anda mengambilnya. Jimat itu terasa hangat di tangan Anda.
""")
        add_item(game_state, "jimat_pelindung")
        game_state.completed_puzzles["simbol_batu"] = True
        pause()
        return hutan_berkabut(game_state)
    
    else:
        clear_screen()
        typewriter_effect("""
Anda salah! Bayangan-bayangan itu bergerak cepat ke arah Anda!

Mereka menyerang! Tapi untung, Anda masih cukup cepat untuk berlari!

Anda menerima 20 damage!
""")
        take_damage(game_state, 20)
        pause()
        return hutan_berkabut(game_state)

def jalur_rawa(game_state: GameState) -> Optional[str]:
    """Jalur Rawa - berbahaya"""
    clear_screen()
    show_status(game_state)
    
    typewriter_effect("""
Jalur rawa ini licin dan berbau busuk. Air hitam mencakup hampir 
seluruh tempat. Anda harus berhati-hati agar tidak jatuh.

Saat Anda berjalan, ada sesuatu yang bergerak di dalam air. 
Sesuatu yang besar. Bayangan panjang di bawah permukaan.

Tiba-tiba, PISAU TUMA yang berkarat muncul dari rawa! 

Anda menangkapnya dengan refleks. Pisau ini... masih bisa digunakan.

Tetapi ada sesuatu yang aneh. Di rawa ini ada juga apa yang tampak 
seperti ARTEFAK HUTAN—benda berkilau aneh yang memancarkan cahaya 
hijau kebiruan.
""")
    
    options = [
        "Ambil PISAU TUA",
        "Ambil ARTEFAK HUTAN (beresiko)",
        "Ambil keduanya",
        "Kembali ke Hutan"
    ]
    
    choice = get_choice(options)
    
    if choice == 1:
        clear_screen()
        typewriter_effect("""
Anda mengambil pisau. Pisau tua ini terasa stabil di tangan Anda.
Mungkin berguna untuk pertempuran nanti.
""")
        add_item(game_state, "pisau_tua")
        pause()
        return hutan_berkabut(game_state)
    
    elif choice == 2:
        clear_screen()
        typewriter_effect("""
Saat Anda mencapai artefak, air rawa mulai menggalak. 
Sesuatu yang besar menarik Anda!

Anda menerima 25 damage saat ditarik sesuatu di air!

Namun Anda berhasil keluar dan mengambil ARTEFAK HUTAN.
""")
        take_damage(game_state, 25)
        add_item(game_state, "artefak_hutan")
        pause()
        return hutan_berkabut(game_state)
    
    elif choice == 3:
        clear_screen()
        typewriter_effect("""
Anda mencoba mengambil keduanya. Saat Anda menggapai artefak, 
sesuatu yang besar menarik Anda dengan sangat kuat!

ARGHHHH! Air membanjiri Anda!

Anda menerima 35 damage!
""")
        take_damage(game_state, 35)
        add_item(game_state, "pisau_tua")
        add_item(game_state, "artefak_hutan")
        pause()
        return hutan_berkabut(game_state)
    
    elif choice == 4:
        return hutan_berkabut(game_state)

def jalan_rahasia(game_state: GameState) -> Optional[str]:
    """Jalan Rahasia - dengan peta"""
    clear_screen()
    show_status(game_state)
    
    typewriter_effect("""
Menggunakan peta, Anda menemukan jalan tersembunyi di antara pohon-pohon.

Jalan ini lebih terang dari yang lain. Kabut di sini tidak seekor tebal. 
Seolah-olah jalan ini dilindungi.

Anda berjalan melewati pohon-pohon besar, dan tiba-tiba, kabut 
membuka celah. Anda menemukan reruntuhan kuno.

Bangunan-bangunan tua, simbol-simbol di dinding. Ini tempat yang 
berbeda dari desa. Ini adalah sisa dari peradaban yang hilang.

Pada kesempatan ini, Anda menemukan CATATAN PANJANG terukir 
di dinding batu utama:

"Kami, orang-orang kuno, telah menutup Gerbang. 
Telah menyegelnya dengan darah dan ritual.
Agar Penghuni tidak keluar.
Setiap generasi, kami memilih satu untuk menjadi JANGKAR.
Jangkar harus ingat kesediaan mereka.
Tetapi untuk melindungi dunia, ingatan harus dihapus.
Desa Senja adalah pengawal kuno kami.
Ritual berlanjut. Tak terbatas. Selamanya."

Anda memahami sekarang—ingatan Anda dihapus karena alasan ini.
""")
    
    game_state.story_flags["tahu_tentang_ritual"] = True
    game_state.story_flags["tahu_nama_di_dinding"] = True
    add_item(game_state, "jurnal_ritual")
    
    options = [
        "Lanjut ke Reruntuhan Kuno",
        "Kembali ke Hutan"
    ]
    
    choice = get_choice(options)
    
    if choice == 1:
        return reruntuhan_kuno(game_state)
    elif choice == 2:
        return hutan_berkabut(game_state)

# ============================================================================
# BAB 3 - RERUNTUHAN KUNO
# ============================================================================

def reruntuhan_kuno(game_state: GameState) -> Optional[str]:
    """Lokasi: Reruntuhan Kuno"""
    game_state.visited_locations["reruntuhan"] = True
    clear_screen()
    show_status(game_state)
    
    if not game_state.story_flags["reruntuhan_pertama_kali"]:
        typewriter_effect("""
Anda memutuskan untuk menuju ke arah selatan desa. Melalui jalur 
yang tersembunyi di antara pohon-pohon, Anda menemukan reruntuhan 
kuno.

Bangunan-bangunan tua berdiri megah meski sudah dalam keadaan 
rusak. Simbol-simbol aneh terukir di setiap sudut. Cahaya moon 
yang aneh bersinar ke bawah, menembus kabut.

Anda merasa seolah-olah Anda telah ke sini sebelumnya, 
tetapi tidak bisa mengingat kapan.
""")
        game_state.story_flags["reruntuhan_pertama_kali"] = True
        pause()
    
    clear_screen()
    show_status(game_state)
    
    typewriter_effect("""
Reruntuhan kuno ini besar sekali. Anda membaca tulisan-tulisan di dinding:

"Gerbang Penghuni"
"Jangan Buka Sebelum Waktunya"
"Mereka yang Mengorbankan Akan Dipilih"

Ada beberapa area yang bisa Anda jelajahi:

1. RUANGAN UTAMA - tempat altar dengan ARTEFAK RUNTUHAN
2. RUANGAN PERPUSTAKAAN - penuh dengan tulisan kuno
3. AREA DASAR - lebih dalam ke bawah reruntuhan
""")
    
    options = [
        "Ambil ARTEFAK RUNTUHAN dari altar",
        "Pelajari tulisan di perpustakaan",
        "Jelajahi area dasar reruntuhan",
        "Kembali ke Desa"
    ]
    
    choice = get_choice(options)
    
    if choice == 1:
        clear_screen()
        typewriter_effect("""
Anda mencoba mengambil artefak. Tapi saat Anda menyentuhnya, 
simbol ritual bersinar merah!

Sesuatu mencengkeram Anda dari bawah tanah! Makhluk shadow 
muncul dari bawah!

SHADOW: "TIDAK! ARTEFAK INI BUKAN MILIKMU!"

Anda bertempur dengan makhluk bayangan!
""")
        pause()
        result = pertarungan_shadow(game_state)
        if result == "menang":
            clear_screen()
            typewriter_effect("""
Anda berhasil mengalahkan makhluk bayangan! 

Anda mengambil ARTEFAK RUNTUHAN dengan tangan bergetar.
""")
            add_item(game_state, "artefak_runtuhan")
        pause()
        return reruntuhan_kuno(game_state)
    
    elif choice == 2:
        clear_screen()
        typewriter_effect("""
Anda mempelajari simbol ritual di perpustakaan. Simbol-simbol ini 
menggambarkan prosesi pengorbanan:

1. PEMILIHAN - Satu orang dipilih
2. PENGASINGAN - Mereka diisolasi dan ingatan dihapus
3. KEMBALI - Mereka dibawa kembali ke desa
4. TRANSISI - Pada saat ritual puncak, mereka menjadi "jangkar" 
   antara dunia nyata dan gerbang yang tersegel

Di dinding lain, Anda membaca:

"NAMA NAMA YANG TERPILIH SEPANJANG SEJARAH:

1823 - Elara Nightwhisper
1856 - Marcus Stone
1892 - Vera Blackwood
1934 - Samuel Cross
1973 - Catherine Veil
2018 - Raven... (nama Anda!)
2023 - AKAN DATANG"

Anda melihat tulisan "Raven" di daftar itu. Anda benar-benar 
adalah bagian dari ritual ini. Sesuatu yang dingin menyelimuti 
jantung Anda.
""")
        game_state.story_flags["tahu_tentang_ritual"] = True
        game_state.story_flags["tahu_nama_di_dinding"] = True
        pause()
        return reruntuhan_kuno(game_state)
    
    elif choice == 3:
        clear_screen()
        typewriter_effect("""
Anda turun lebih dalam ke bawah reruntuhan. Jalan menjadi semakin 
sempit. Cahaya mulai menghilang.

Saat Anda memasuki goa di bawah reruntuhan, Anda melihat cahaya 
aneh yang memancar dari dalam. Cahaya yang berkilau dengan warna 
tidak alami.

Anda menemukan JURNAL RITUAL - buku tua yang dipenuhi catatan 
tentang ritual dan pengorbanan.

Bacaan dari jurnal ini menceritakan kebenaran tentang Desa Senja 
dan makhluk yang dijaga oleh orang-orang kuno. Anda baru memahami 
betapa serius situasi ini.
""")
        add_item(game_state, "jurnal_ritual")
        game_state.story_flags["tahu_tentang_ritual"] = True
        pause()
        return reruntuhan_kuno(game_state)
    
    elif choice == 4:
        return None

def pertarungan_shadow(game_state: GameState) -> str:
    """Sistem pertarungan sederhana berbasis teks"""
    clear_screen()
    
    enemy_hp = 50
    enemy_name = "Makhluk Bayangan"
    
    typewriter_effect(f"""
Pertempuran dimulai!

{enemy_name} HP: {enemy_hp}
Anda HP: {game_state.hp}
""")
    
    while game_state.hp > 0 and enemy_hp > 0:
        options = [
            "Serang dengan pisau (jika punya)",
            "Gunakan jimat untuk perlindungan",
            "Coba berlari",
            "Pertahankan diri"
        ]
        
        choice = get_choice(options)
        
        if choice == 1:
            if check_inventory_item(game_state, "pisau_tua"):
                damage = random.randint(15, 30)
                enemy_hp -= damage
                typewriter_effect(f"\n⚔️  Anda menyerang dengan pisau! Damage: {damage}")
            else:
                damage = random.randint(5, 15)
                enemy_hp -= damage
                typewriter_effect(f"\n👊 Anda pukulan dengan tangan! Damage: {damage}")
        
        elif choice == 2:
            if check_inventory_item(game_state, "jimat_pelindung"):
                typewriter_effect(f"\n🛡️  Jimat melindungi Anda! Anda menghindari serangan!")
            else:
                damage = random.randint(10, 20)
                game_state.hp -= damage
                typewriter_effect(f"\n💥 Anda tidak punya jimat! Menerima {damage} damage!")
        
        elif choice == 3:
            typewriter_effect(f"\n🏃 Anda berlari!")
            return "lari"
        
        elif choice == 4:
            damage_taken = random.randint(5, 15)
            game_state.hp -= damage_taken
            typewriter_effect(f"\n🛡️  Anda bertahan, menerima {damage_taken} damage")
        
        if enemy_hp > 0:
            damage_to_player = random.randint(10, 25)
            game_state.hp -= damage_to_player
            typewriter_effect(f"\n{enemy_name} menyerang! Damage: {damage_to_player}")
        
        print(f"\n{enemy_name} HP: {enemy_hp} | Anda HP: {game_state.hp}")
        
        if game_state.hp <= 0:
            clear_screen()
            typewriter_effect("""
Anda terjatuh. Kesadaran Anda memudar.

Tetapi... Anda tidak mati. Malah, Anda terbangun kembali di desa.
Di rumah yang sama. Saat yang sama.

Ini bagian dari ritual? Apakah Anda bisa mati di dunia ini?
""")
            game_state.hp = 50  # HP reset
            return "kalah"
        
        pause()
    
    return "menang"

# ============================================================================
# BAB 4 - GUA TERLARANG
# ============================================================================

def gua_terlarang(game_state: GameState) -> Optional[str]:
    """Lokasi: Gua Terlarang - jantung misteri"""
    game_state.visited_locations["gua"] = True
    clear_screen()
    show_status(game_state)
    
    if not game_state.story_flags["gua_pertama_kali"]:
        typewriter_effect("""
Anda meninggalkan desa dan melangkah ke arah utara yang gelap. 
Kabut semakin tebal. Suara bisikan semakin keras.

Setelah berjalan menembus kegelapan, Anda menemukan lubang besar 
di dalam tanah. Sebuah gua yang misterius. Cahaya aneh bersinar 
dari dalam.

Sesuatu di dalam gua itu terasa... hidup. Terasa mengamati Anda.

Anda menemukan obor tua di depan gua (jika belum punya). 
Cahayanya akan membantu Anda menerangi kegelapan di dalam.
""")
        game_state.story_flags["gua_pertama_kali"] = True
        pause()
    
    clear_screen()
    show_status(game_state)
    
    typewriter_effect("""
Gua Terlarang terletak di depan Anda, gelap dan menakutkan.

Dinding gua penuh dengan ukiran—ribuan nama. Nama-nama orang yang 
telah dipilih sepanjang sejarah. Dan di antara ribuan nama itu, 
Anda melihat nama Anda sendiri terukir di sana:

RAVEN - 2023

Semakin dalam Anda pergi, suara bisikan semakin keras. 
Ribuan suara, semuanya memanggil Anda dengan nama.

Akhirnya, Anda sampai ke ruangan besar. Di tengahnya, 
sebuah cahaya yang sangat terang. Cahaya yang mengancam jiwa Anda.

Ada dua pilihan:
1. Lanjut ke dalam untuk bertemu Penghuni Gerbang (ENDING TERTINGGI)
2. Ambil item dan periksa tulisan lebih dulu
3. Kembali ke Desa
""")
    
    options = [
        "Mendekat ke cahaya dan bertemu Penghuni",
        "Gunakan obor untuk melindungi diri dan ambil ARTEFAK INTI",
        "Baca tulisan di dinding gua",
        "Kembali ke Desa"
    ]
    
    choice = get_choice(options)
    
    if choice == 1:
        return inti_misteri(game_state)
    elif choice == 2:
        clear_screen()
        if check_inventory_item(game_state, "obor"):
            typewriter_effect("""
Anda menggunakan obor. Cahaya oranye obor bertemu cahaya aneh dari 
tengah gua. 

Cahaya itu menghilang sejenak. Anda melihat—di tengah ruangan, 
ada sebuah ARTEFAK INTI. Benda ini adalah sumber cahaya itu.

Dengan hati-hati, Anda mengambilnya. Energi dari artefak ini 
terasa sangat kuat di tangan Anda.
""")
            add_item(game_state, "artefak_inti")
        else:
            typewriter_effect("""
Anda tidak memiliki obor untuk melindungi diri. Cahaya itu 
sangat terang dan menyakitkan mata Anda!

Anda menerima 15 damage karena intensitas cahaya!
""")
            take_damage(game_state, 15)
        pause()
        return gua_terlarang(game_state)
    elif choice == 3:
        clear_screen()
        typewriter_effect("""
Anda membaca tulisan di dinding:

"INI ADALAH GERBANG. GERBANG KE DUNIA LAIN.

Di sebaliknya, ada makhluk yang kami sebut: PENGHUNI GERBANG.

Makhluk ini sangat kuno. Lebih tua dari peradaban kami. 
Lebih tua dari dunia ini.

Kami telah menyegelnya dengan ritual dan pengorbanan. 
Setiap generasi, kami mengambil satu 'jangkar'—seseorang yang bisa 
merasakan kedua dunia.

Jangkar itu akan menjadi penghubung antara dunia nyata dan sisi lain. 
Mereka akan menjadi kunci untuk menjaga segel itu tetap kuat.

Ini adalah nasib yang dipilih untuk mereka. Nasib yang tidak bisa 
dihindari.

Tetapi... ada cara untuk memecahkan siklus ini. 
Ada cara untuk membebaskan Penghuni.
Ada cara untuk membebaskan diri sendiri.

Jawaban ada di hati seseorang yang terpilih.
Jawaban ada pada pilihan yang mereka buat."

Anda memahami sekarang. Semuanya tergantung pada pilihan Anda.
""")
        game_state.story_flags["tahu_tentang_ritual"] = True
        pause()
        return gua_terlarang(game_state)
    elif choice == 4:
        return None

def inti_misteri(game_state: GameState) -> Optional[str]:
    """Area Akhir - Penemu Penghuni Gerbang"""
    game_state.visited_locations["inti_misteri"] = True
    clear_screen()
    show_status(game_state)
    
    typewriter_effect("""
Cahaya itu mulai berubah bentuk. Cahaya yang terang menjadi 
siluet. Siluet itu menjadi makhluk.

Makhluk itu tidak seperti apa pun yang pernah Anda lihat. 
Tidak sepenuhnya nyata. Seperti bayangan yang memiliki jiwa.

PENGHUNI: "Akhirnya... akhirnya Anda datang ke sini, Raven."

Suara itu terdengar di mana-mana. Di dalam kepala Anda. 
Di dalam hati Anda.

PENGHUNI: "Aku telah menunggu selama berabad-abad. Tertahan di sisi 
lain segel. Mendengar bisikan ribuan jangkar. Merasakan kesedihan 
mereka yang dipilih untuk mengikatku."

PENGHUNI: "Tetapi Anda berbeda, Raven. Anda memiliki kesempatan 
untuk membuat pilihan yang belum pernah dibuat sebelumnya."

Makhluk itu melangkah lebih dekat. Energinya terasa sangat kuat.

PENGHUNI: "Aku bisa merasakan keputusan Anda. Aku menunggu."

Anda memiliki empat pilihan. Setiap pilihan akan mengubah takdir 
desa ini. Takdir Anda. Takdir dunia ini.
""")
    
    pause()
    
    options = [
        "Perkuat segel (Ending Baik - Desa selamat, Anda hilang)",
        "Buka segel sepenuhnya (Ending Buruk - Dunia dalam bahaya)",
        "Pergi tanpa memilih (Ending Misteri - Menunggu generasi berikutnya)",
        "Ubah ritual (Ending Rahasia - Butuh semua artefak)"
    ]
    
    choice = get_choice(options)
    
    if choice == 1:
        return ending_baik(game_state)
    elif choice == 2:
        return ending_buruk(game_state)
    elif choice == 3:
        return ending_misteri(game_state)
    elif choice == 4:
        return ending_rahasia(game_state)

# ============================================================================
# ENDING
# ============================================================================

def ending_baik(game_state: GameState):
    """Ending Baik - Segel diperkuat, Raven hilang"""
    clear_screen()
    typewriter_effect("""
ENDING BAIK: PENGORBANAN UNTUK KESELAMATAN

Anda membuat keputusan. Anda tidak ingin dunia jatuh ke tangan 
makhluk itu. Anda tidak ingin lebih banyak desa yang terikat.

Anda membentuk ritual yang lebih kuat. Anda menggunakan artefak 
yang Anda kumpulkan. Anda memanggil kekuatan dari semua jangkar 
sebelumnya.

Cahaya bersinar dengan terang yang membutakan. 

PENGHUNI: "Tidak... tidak begini... RAVEN!!!"

Segel yang baru menjadi jauh lebih kuat dari sebelumnya. 
Penghuni tersimpan lebih dalam. Lebih jauh. Mungkin selamanya.

Tetapi harganya... harga yang harus dibayar adalah hidupmu.

Tubuh Anda mulai bersinar. Anda menjadi bagian dari segel itu. 
Anda adalah jangkar final. Jangkar yang paling kuat.

Anda merasa tubuh Anda meleleh. Ingatan Anda hilang kembali. 
Tetapi kali ini, Anda melakukannya dengan sukarela.

Saat kesadaran Anda hilang, Anda mendengar suara tetua desa:

TETUA DESA: "Raven telah mengorbankan diri. Desa selamat. 
Ritual akan berlanjut. Tetapi lebih aman sekarang. 
Berkat Raven, kami akan hidup lebih lama."

---

Anda telah mencapai ENDING BAIK.

Desa selamat, tetapi Anda hilang dari dunia. 
Anda menjadi legenda. Anda menjadi perlindungan.

Suatu hari, akan ada yang lain yang dipilih. 
Dan mereka akan memiliki kesempatan yang sama dengan yang Anda miliki.
""")
    pause()

def ending_buruk(game_state: GameState):
    """Ending Buruk - Segel terbuka, Penghuni lepas"""
    clear_screen()
    typewriter_effect("""
ENDING BURUK: GERBANG TERBUKA

Anda membuat pilihan. Rasa kasihan kepada makhluk yang terikat 
berabad-abad mengalahkan akal sehat Anda.

Anda membuka segel.

PENGHUNI: "AKHIRNYA!!! AKHIRNYA KAMI BEBAS!!!"

Makhluk itu meledak keluar dengan energi yang menghancurkan. 
Gua berguncang. Batu-batu jatuh.

Anda berlari, tetapi tubuh Anda sudah terlalu lemah. 
Anda jatuh.

Saat Anda jatuh, Anda melihat—di balik Penghuni—ada lebih banyak 
makhluk. Jauh lebih banyak. Ribuan. Jutaan.

Mereka semua keluar.

---

Anda terbangun di rumah Anda di desa. Tetapi semuanya berbeda.

Kabut yang sebelumnya di sekitar desa sekarang menyebar ke mana-mana. 
Dunia berada dalam kegelapan. Makhluk-makhluk aneh berkeliaran.

Orang-orang di kota tetangga menghubungi. Mereka mengatakan 
hal yang sama terjadi di sana. Dan di sana. Dan di sana.

Anda menyadari—Anda telah membuka gerbang bukan hanya untuk 
satu makhluk, tetapi untuk semua makhluk yang ada di baliknya.

Dunia sedang berakhir.

---

Anda telah mencapai ENDING BURUK.

Desa mungkin selamat untuk saat ini, tetapi dunia... 
dunia sedang jatuh ke dalam kegelapan yang tak terbatas.

Adakah cara untuk menutup gerbang itu kembali?
Atau apakah sudah terlambat?
""")
    pause()

def ending_misteri(game_state: GameState):
    """Ending Misteri - Tidak memilih"""
    clear_screen()
    typewriter_effect("""
ENDING MISTERI: PENUNDAAN TAKDIR

Anda tidak membuat pilihan apapun. Anda hanya meninggalkan Penghuni 
sendiri di sana.

PENGHUNI: "Anda tidak memilih? Bagaimana mungkin..."

Anda berbalik dan pergi dari gua itu. Anda melangkah keluar dari 
reruntuhan kuno. Anda meninggalkan hutan berkabut.

Anda kembali ke desa. Semuanya sama seperti sebelumnya. 
Penduduk masih duduk di balai, tersenyum aneh.

TETUA DESA: "Anda telah kembali, Raven. Tetapi... Anda tidak 
menyelesaikan ritual?"

ANDA: "Saya tidak tahu apa yang seharusnya saya lakukan."

Tetua tersenyum dengan aneh.

TETUA DESA: "Baiklah. Jika begitu, desa akan menunggu. 
Menunggu hingga Anda siap. Atau menunggu yang dipilih berikutnya."

---

Hari-hari berlalu. Minggu berlalu. Tahun berlalu.

Anda tetap tinggal di desa. Ingatan Anda tetap hilang. 
Anda menjadi seperti penduduk desa lainnya.

Tetapi ada sesuatu yang berbeda. Anda tahu kebenaran. 
Anda tahu tentang segel. Anda tahu tentang Penghuni.

Suatu hari, seseorang datang ke desa. Seseorang baru. 
Seseorang yang tersesat di kabut.

Tetua desa tersenyum.

TETUA DESA: "Aku percaya telah tiba waktunya, Raven. 
Untuk generasi baru. Untuk yang dipilih berikutnya."

Siklus berulang.

---

Anda telah mencapai ENDING MISTERI.

Desa tetap ada. Ritual tetap berlanjut. 
Tetapi Anda sekarang menjadi bagian dari desa. 
Bagian dari siklus yang tak terbatas.

Adakah jalan keluar? Atau adakah yang akan menemukan jalan keluar 
di generasi mendatang?
""")
    pause()

def ending_rahasia(game_state: GameState):
    """Ending Rahasia - Ubah ritual dengan semua artefak"""
    clear_screen()
    
    # Check if all artifacts are collected
    has_all_artifacts = (
        check_inventory_item(game_state, "artefak_hutan") and
        check_inventory_item(game_state, "artefak_runtuhan") and
        check_inventory_item(game_state, "artefak_inti")
    )
    
    has_all_puzzles = (
        game_state.completed_puzzles["simbol_batu"] and
        game_state.completed_puzzles["ritual_simbol"]
    )
    
    if has_all_artifacts and has_all_puzzles and game_state.hp > 0:
        typewriter_effect("""
ENDING RAHASIA: MEMECAHKAN SIKLUS

Anda telah mengumpulkan semua artefak kuno. Anda telah menyelesaikan 
semua teka-teki. Anda masih hidup. Anda siap.

Anda menempatkan ketiga artefak di depan Penghuni. 
Cahaya mereka bersatu dan bersinar.

PENGHUNI: "Apa ini? Apa yang Anda lakukan?"

Anda memulai ritual yang berbeda. Ritual yang tidak mengutamakan 
pengorbanan, tetapi pemahaman.

Anda menyentuh Penghuni dengan tangan Anda. 

Bukan serangan. Bukan penjara. Tetapi koneksi.

Ingatan mengalir. Ingatan Penghuni. Ingatan tentang dunia sebelum segel. 
Ingatan tentang peradaban yang hilang. Ingatan tentang cinta, 
harapan, dan kepercayaan yang hilang.

Anda memahami Penghuni sekarang. Bukan sebagai musuh. Tetapi sebagai 
makhluk yang kesepian. Makhluk yang lupa siapa dirinya.

PENGHUNI: "Anda memahami saya. Bagaimana mungkin..."

ANDA: "Karena saya juga lupa. Tetapi sekarang, saya mengingat."

Ingatan Anda kembali. Semua itu. Wajah Anda, nama Anda, 
kehidupan Anda sebelum desa.

Anda bukan Raven yang dipilih tahun ini. Anda adalah Raven 
dari lima tahun yang lalu. Orang yang melihat kebenaran dan 
ditghapus ingatannya.

Dan sekarang, pada saat ini, ritual berubah.

Segel itu tidak dihancurkan. Tetapi juga tidak diperkuat. 
Sebaliknya, segel itu menjadi pintu dua arah. Penghuni dan dunia 
nyata dapat saling memahami.

Desa Senja dibebaskan dari keharusan pengorbanan. 
Mereka dapat hidup dengan damai.

Anda dan Penghuni—kalian berdua menjadi duta antara dua dunia. 
Simbol dari perdamaian yang mungkin dicapai.

---

Anda telah mencapai ENDING RAHASIA: PEMBEBASAN.

Desa selamat. Penghuni selamat. 
Dunia selamat karena ada pemahaman, bukan pengorbanan.

Ingatan Anda kembali. Identitas Anda dikembalikan.

Ritual berakhir. Siklus putus.

Ini adalah ending yang paling langka. Ending yang memerlukan 
kearifan, keberanian, dan pemberian maaf.

Selamat, Raven. Anda telah mengubah takdir.
""")
    else:
        clear_screen()
        typewriter_effect("""
Anda mencoba membuat ritual baru, tetapi...

Artefak Anda tidak cukup. Pengetahuan Anda belum lengkap. 
Tubuh Anda terlalu lemah.

Ritual yang Anda coba ciptakan malah menghasilkan sesuatu yang 
tidak terduga. Cahaya meledak.

Anda terpukul kuat ke belakang. Consciousness Anda memudar.

---

Anda terbangun di rumah Anda di desa. Seperti sebelumnya.

Tetua desa tersenyum.

TETUA DESA: "Anda mencoba sesuatu yang tidak seharusnya, Raven. 
Ritual tidak dapat diubah oleh siapa pun. Tidak bahkan oleh 
yang terpilih."

Anda kembali ke pilihan pertama. Anda harus membuat keputusan: 
perkuat, buka, atau tinggalkan?

---

Anda harus mencoba lagi dengan persiapan yang lebih baik.
""")
        pause()
        return inti_misteri(game_state)
    
    pause()

# ============================================================================
# MENU UTAMA & LOOP GAME
# ============================================================================

def main_menu():
    """Menu utama game"""
    clear_screen()
    typewriter_effect("""
╔═══════════════════════════════════════════════════════════════╗
║                  BISIKAN DARI KABUT                          ║
║              Sebuah Petualangan Penuh Misteri                ║
╚═══════════════════════════════════════════════════════════════╝

Pilihan:
1. Mulai Game Baru
2. Tentang Game
3. Keluar
""")
    
    options = ["Mulai Game", "Tentang", "Keluar"]
    choice = get_choice(options)
    
    if choice == 1:
        return "main_game"
    elif choice == 2:
        clear_screen()
        typewriter_effect("""
TENTANG GAME:

"Bisikan dari Kabut" adalah game petualangan teks dengan tema 
misteri dan horror yang ringan.

Cerita:
Anda terbangun di sebuah desa yang tertutup kabut tebal. 
Penduduk desa berbicara dengan kata-kata aneh. Ada ritual kuno 
yang mengikat desa ini ke makhluk misterius.

Anda adalah bagian dari ritual itu, dan Anda harus membuat 
pilihan yang akan mengubah takdir Anda dan dunia.

Fitur:
- Multiple endings (4 berbeda)
- Sistem inventory dan HP
- Pertarungan berbasis teks
- Puzzle dan teka-teki
- Alur cerita yang bercabang

Developer: AI Programmer
Bahasa: Python 3
""")
        pause()
        return "menu_utama"
    elif choice == 3:
        return "keluar"

def main_game(game_state: GameState):
    """Loop permainan utama"""
    prolog(game_state)
    
    # Game loop - Pemain bisa memilih lokasi bebas
    while game_state.hp > 0:
        clear_screen()
        show_status(game_state)
        
        typewriter_effect("""
Anda berada di Desa Senja. Kabut tebal mengelilingi Anda, dan ada 
beberapa arah yang bisa Anda jelajahi. Setiap arah akan membawa 
Anda ke petualangan yang berbeda...

PILIH LOKASI UNTUK DIJELAJAHI:
""")
        
        options = [
            "Jelajahi Desa Lebih Jauh (Balai, Rumah, Sumur, Lonceng)",
            "Pergi ke Hutan Berkabut (Barat)",
            "Pergi ke Reruntuhan Kuno (Selatan)",
            "Pergi ke Gua Terlarang (Bawah Tanah)"
        ]
        choice = get_choice(options)
        
        if choice == 1:
            desa_terlupakan(game_state)
        elif choice == 2:
            hutan_berkabut(game_state)
        elif choice == 3:
            reruntuhan_kuno(game_state)
        elif choice == 4:
            gua_terlarang(game_state)
        
        if game_state.hp <= 0:
            break

def main():
    """Main function - entry point"""
    state = "menu_utama"
    game_state = GameState()
    
    while state != "keluar":
        if state == "menu_utama":
            state = main_menu()
        elif state == "main_game":
            main_game(game_state)
            state = "menu_utama"
    
    clear_screen()
    typewriter_effect("""
Terima kasih telah bermain BISIKAN DARI KABUT!

Semoga Anda menikmati perjalanan di dunia yang penuh misteri ini.

Kabut akan selalu di sini... menunggu Anda kembali...
""")
    print("\n")

if __name__ == "__main__":
    main()
