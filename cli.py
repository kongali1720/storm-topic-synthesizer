from storm_core.retriever import get_references
from storm_core.synthesizer import generate_outline

def main():
    print("🔍 STORM — Topic Outline Generator")
    topic = input("Masukkan topik utama: ")
    print("⏳ Mengambil referensi...")
    refs = get_references(topic)
    print("🧠 Menghasilkan outline dengan GPT...")
    outline = generate_outline(topic, refs)
    print("\n📄 Hasil Outline:")
    print(outline)

if __name__ == "__main__":
    main()
