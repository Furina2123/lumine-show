import os # Ajoute ça en haut
import asyncio
import websockets

# ... (le reste de ton code CLIENTS = set() etc.)

async def main():
    # Railway donne le port via une variable d'environnement
    port = int(os.environ.get("PORT", 8001)) 
    print(f"⚡ SERVEUR LUMINE PRO lancé sur le port {port}")
    async with websockets.serve(handler, "0.0.0.0", port):
        await asyncio.Future() 

if __name__ == "__main__":
    asyncio.run(main())