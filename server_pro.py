import asyncio
import websockets
import os
import json

# On garde une liste de tous les gens connectés (téléphones + admin)
CLIENTS = set()

async def handler(websocket):
    # Quand quelqu'un se connecte, on l'ajoute à la liste
    CLIENTS.add(websocket)
    print(f"Connexion établie ! Total : {len(CLIENTS)}")
    
    try:
        async for message in websocket:
            # Quand l'admin envoie une couleur, on la renvoie à TOUT LE MONDE
            if CLIENTS:
                # On crée une copie pour éviter les erreurs si quelqu'un se déconnecte pendant l'envoi
                await asyncio.gather(*(client.send(message) for client in CLIENTS))
    except websockets.exceptions.ConnectionClosed:
        pass
    finally:
        # Quand quelqu'un part, on l'enlève de la liste
        CLIENTS.remove(websocket)
        print(f"Déconnexion. Restants : {len(CLIENTS)}")

async def main():
    # Railway donne le port via cette variable d'environnement
    port = int(os.environ.get("PORT", 8080))
    
    print(f"⚡ SERVEUR LUMINE PRO lancé sur le port {port}")
    
    # On lance le serveur sur 0.0.0.0 pour qu'il soit accessible de l'extérieur
    async with websockets.serve(handler, "0.0.0.0", port):
        await asyncio.Future()  # Garde le serveur allumé indéfiniment

if __name__ == "__main__":
    asyncio.run(main())
