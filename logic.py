import aiohttp  # Eşzamansız HTTP istekleri için bir kütüphane
import random
import asyncio
from datetime import datetime, timedelta
import time

class Pokemon:
    pokemons = {}
    # Nesne başlatma (kurucu)
    def __init__(self, pokemon_trainer):
        self.pokemon_trainer = pokemon_trainer
        self.pokemon_number = random.randint(1, 1000)
        self.name = None #self.pokemon_number
        if pokemon_trainer not in Pokemon.pokemons:
            Pokemon.pokemons[pokemon_trainer] = self
        else:
            self = Pokemon.pokemons[pokemon_trainer]

    async def get_name(self):
        # PokeAPI aracılığıyla bir pokémonun adını almak için eşzamansız bir yöntem
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'  # İstek için URL API'si
        async with aiohttp.ClientSession() as session:  # Bir HTTP oturumu açma
            async with session.get(url) as response:  # GET isteği gönderme
                if response.status == 200:
                    data = await response.json()  # JSON yanıtının alınması ve kodunun çözülmesi
                    return data['forms'][0]['name']  # Bir Pokémon'un adını döndürme
                else:
                    return "Pikachu"  # İstek başarısız olursa varsayılan adı döndürür

    async def info(self):
        # Pokémon hakkında bilgi döndüren bir metot
        if not self.name:
            self.name = await self.get_name()  # Henüz yüklenmemişse bir adın geri alınması
            self.hp = await self.get_hp()
            self.attack = await self.get_attack()
            self.defense = await self.get_defense()
            self.specialDefense = await self.get_specialDefense()
            self.last_feed_time = datetime.now()
        return f"Pokémonunuzun ismi: {self.name}\nPokémonunuzun canı: {self.hp}\nPokémonunuzun atağı: {self.attack}\nPokémonunuzun savunması: {self.defense}\nPokémonunuzun özel savunması: {self.specialDefense}\n"  # Pokémon'un adını içeren dizeyi döndürür

    async def show_img(self):
        # PokeAPI aracılığıyla bir pokémon görüntüsünün URL'sini almak için eşzamansız bir yöntem
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'  # İstek için URL API'si
        async with aiohttp.ClientSession() as session:  # Bir HTTP oturumu açma
            async with session.get(url) as response:  # GET isteği gönderme
                if response.status == 200:
                    data = await response.json()  # JSON yanıtının alınması ve kodunun çözülmesi
                    return data['sprites']['front_default']  # Bir Pokémon'un resmini döndürme
                else:
                    return "Something went wrong." # İstek başarısız olursa varsayılan adı döndürür
                
    async def get_hp(self):
        # PokeAPI aracılığıyla bir pokémon HP'sinin URL'sini almak için eşzamansız bir yöntem
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'  # İstek için URL API'si
        async with aiohttp.ClientSession() as session:  # Bir HTTP oturumu açma
            async with session.get(url) as response:  # GET isteği gönderme
                if response.status == 200:
                    data = await response.json()  # JSON yanıtının alınması ve kodunun çözülmesi
                    return data['stats'][0]['base_stat'] * 5  # Bir Pokémon'un canını döndürme
                else:
                    return "Something went wrong." # İstek başarısız olursa varsayılan adı döndür
                
    async def get_attack(self):
        # PokeAPI aracılığıyla bir pokémon HP'sinin URL'sini almak için eşzamansız bir yöntem
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'  # İstek için URL API'si
        async with aiohttp.ClientSession() as session:  # Bir HTTP oturumu açma
            async with session.get(url) as response:  # GET isteği gönderme
                if response.status == 200:
                    data = await response.json()  # JSON yanıtının alınması ve kodunun çözülmesi
                    return data['stats'][1]['base_stat']  # Bir Pokémon'un atağını döndürme
                else:
                    return "Something went wrong." # İstek başarısız olursa varsayılan adı döndür
                    
    async def get_defense(self):
        # PokeAPI aracılığıyla bir pokémon HP'sinin URL'sini almak için eşzamansız bir yöntem
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'  # İstek için URL API'si
        async with aiohttp.ClientSession() as session:  # Bir HTTP oturumu açma
            async with session.get(url) as response:  # GET isteği gönderme
                if response.status == 200:
                    data = await response.json()  # JSON yanıtının alınması ve kodunun çözülmesi
                    return data['stats'][2]['base_stat']  # Bir Pokémon'un savunmasını döndürme
                else:
                    return "Something went wrong." # İstek başarısız olursa varsayılan adı döndür

    async def get_specialDefense(self):
        # PokeAPI aracılığıyla bir pokémon HP'sinin URL'sini almak için eşzamansız bir yöntem
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'  # İstek için URL API'si
        async with aiohttp.ClientSession() as session:  # Bir HTTP oturumu açma
            async with session.get(url) as response:  # GET isteği gönderme
                if response.status == 200:
                    data = await response.json()  # JSON yanıtının alınması ve kodunun çözülmesi
                    return data['stats'][4]['base_stat']  # Bir Pokémon'un özel savunmasını döndürme
                else:
                    return "Something went wrong." # İstek başarısız olursa varsayılan adı döndür

    async def damage(self, enemy):
        if isinstance(enemy, Wizard):
            x = random.randint(1, 5)
            if x == 1:
                return f"{self.name}, {enemy.name} rakibinin kalkanını kıramadı.{enemy.name} hasar almadı"

        if enemy.hp > self.attack:
            enemy.hp -= self.attack
            return f"{self.name}, {self.attack} HP kadar güçlü bir saldırıda bulundu.\n{enemy.name} ismindeki rakibinin HP'si {enemy.hp} oldu."
        else:
            return f"{self.name}, {self.attack} HP kadar güçlü bir saldırıda bulundu.\n{enemy.name} ismindeki rakip kaybetti."

    async def feed(self, feed_interval=20, hp_increase=10):
        current_time = datetime.now()
        delta_time = timedelta(seconds=feed_interval)
        if (current_time - self.last_feed_time) > delta_time:
            self.hp += hp_increase
            self.last_feed_time = current_time
            return f"Pokémon'un sağlığı geri yüklenir. Mevcut sağlık: {self.hp}"
        else:
            return f"Pokémonunuzu şu zaman besleyebilirsiniz: {current_time+delta_time}"    


class Fighter(Pokemon):
    async def damage(self, enemy):
        x = random.randint(0, 20)
        self.attack += x 
        result = await super().damage(enemy)
        self.attack -= x
        return f"{result}, atağı {x} kadar arttı ama."
    async def feed(self, hp_increase = 10, feed_interval=20):
        hp_increase += random.randint(10, 20)
        return await super().feed(feed_interval, hp_increase)


        
    
 
class Wizard(Pokemon):
    async def feed(self, feed_interval = 20, hp_increase = 10):
        feed_interval -= random.randint(5, 15)
        return await super().feed(feed_interval, hp_increase)


# ------------- TESTING -----------------

if __name__ == "__main__":
    async def a():
        z = {"Sander": "A"}
        trainer1 = Wizard("Sander")
        trainer2 = Fighter("Mehmet")
        y = z["Sander"]
        print(await trainer1.info())
        print(await trainer2.info())
        print("***--------------------------****------------------------------***")
        print(await trainer1.damage(trainer2))
        print("----------------")
        print(await trainer2 .damage(trainer1))
        print("------------------")
        print(await trainer1.feed())
        time.sleep(21)
        print(await trainer1.feed())

    asyncio.run(a())