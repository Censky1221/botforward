from telethon import TelegramClient, events
import asyncio

api_id = '26571067'
api_hash = '75616f6d77b6768c012db3b4a9b0b08d'

client = TelegramClient('session_name', api_id, api_hash)

# Channel sumber pesan
source_channel = '@promotelistcensky'  # Ganti dengan username channel kamu (tanpa @)

# Daftar grup tujuan
target_groups = [-1001972064907, -1001549789259, -1001605348889, -1001959015060, -1001599377611, -1001451274472, -1002065024982, -1001768384705, -1001919692847,]

async def get_all_messages_from_channel(channel):
    pesan_list = []
    async for message in client.iter_messages(channel, reverse=True):
        pesan_list.append(message)
    return pesan_list

async def kirim_pesan_ke_grup(client, group_id, pesan):
    try:
        # Meneruskan pesan langsung dari channel ke grup
        await client.forward_messages(
            entity=group_id,
            messages=pesan.id,
            from_peer=pesan.peer_id
        )
        print(f"✅ Berhasil meneruskan pesan ke: {group_id}")
    except Exception as e:
        print(f"❌ Gagal meneruskan pesan ke {group_id}. Error: {e}")

async def main():
    try:
        await client.start()
        while True:  # Pengulangan tanpa batas
            pesan_list = await get_all_messages_from_channel(source_channel)

            for pesan in pesan_list:
                if pesan.text:  # Memastikan pesan memiliki konten
                    for group_id in target_groups:
                        await kirim_pesan_ke_grup(client, group_id, pesan)
                    print("⏳ Menunggu 15 menit sebelum mengirim pesan berikutnya...")
                    await asyncio.sleep(900)  # Tunggu 15 menit sebelum mengirim pesan berikutnya
    finally:
        await client.disconnect()

if __name__ == "__main__":
    client.loop.run_until_complete(main())


