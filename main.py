import asyncio
import aiomysql
import datetime
import random
import logging
import discord
from discord.ext import commands
from discord import SelectOption, ui, Interaction, Embed
from discord.ui import Select, View
import os
from dotenv import load_dotenv
from keep_alive import keep_alive
import shutil

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

print("aiomysql is installed and working!")

intents = discord.Intents().all()
intents.message_content = True
intents.members = True

keep_alive()

bot = commands.Bot(command_prefix='?', intents=intents)

elo_emoji = "<:Elo:1289528803462217748>"

import asyncio
import aiomysql
import logging
import discord
from discord.ext import commands
from dotenv import load_dotenv
from keep_alive import keep_alive

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

print("aiomysql is installed and working!")

intents = discord.Intents().all()
intents.message_content = True
intents.members = True

keep_alive()

bot = commands.Bot(command_prefix='?', intents=intents)

elo_emoji = "<:Elo:1289528803462217748>"

# Informations MySQL
MYSQL_HOST = "sql209.infinityfree.com"
MYSQL_USER = "if0_38099598"
MYSQL_PASSWORD = "4bhv2sctOAw"
MYSQL_DATABASE = "if0_38099598_bot_db"

@bot.event
async def on_ready():
    logging.info('Bot is ready.')

    try:
        # Connexion à la base de données MySQL
        pool = await aiomysql.create_pool(
            host=MYSQL_HOST,
            user=MYSQL_USER,
            password=MYSQL_PASSWORD,
            db=MYSQL_DATABASE,
            port=3306
        )

        async with pool.acquire() as conn:
            async with conn.cursor() as cursor:
                # Création des tables si elles n'existent pas déjà
                await cursor.execute('''CREATE TABLE IF NOT EXISTS user_stats (
                    user_id BIGINT PRIMARY KEY,
                    force INT DEFAULT 5,
                    vitesse INT DEFAULT 5,
                    resistance INT DEFAULT 5,
                    endurance INT DEFAULT 5,
                    agilite INT DEFAULT 5,
                    combat INT DEFAULT 5,
                    FDD INT DEFAULT 0,
                    haki_armement INT DEFAULT 0,
                    haki_observation INT DEFAULT 0,
                    haki_rois INT DEFAULT 0,
                    points INT DEFAULT 0,
                    points_spent INT DEFAULT 0
                )''')
                await cursor.execute('''CREATE TABLE IF NOT EXISTS fdd_inventory (
                    user_id BIGINT,
                    fdd_name VARCHAR(255) UNIQUE,
                    description TEXT,
                    eaten ENUM('True', 'False') DEFAULT 'False',
                    PRIMARY KEY (user_id, fdd_name),
                    FOREIGN KEY (user_id) REFERENCES user_stats (user_id)
                )''')
                await cursor.execute('''CREATE TABLE IF NOT EXISTS user_decorations (
                    user_id BIGINT PRIMARY KEY,
                    thumbnail_url TEXT,
                    icon_url TEXT,
                    main_url TEXT,
                    color VARCHAR(7) DEFAULT '#FFBF66',
                    ost_url TEXT,
                    FOREIGN KEY (user_id) REFERENCES user_stats (user_id)
                )''')
                await cursor.execute('''CREATE TABLE IF NOT EXISTS skills (
                    user_id BIGINT,
                    ittoryu INT DEFAULT 0,
                    nitoryu INT DEFAULT 0,
                    santoryu INT DEFAULT 0,
                    mutoryu INT DEFAULT 0,
                    style_du_renard_de_feu INT DEFAULT 0,
                    danse_de_lepee_des_remous INT DEFAULT 0,
                    style_de_combat_tireur_delite INT DEFAULT 0,
                    balle_explosive INT DEFAULT 0,
                    balle_incendiaire INT DEFAULT 0,
                    balle_fumigene INT DEFAULT 0,
                    balle_degoutante INT DEFAULT 0,
                    balle_cactus INT DEFAULT 0,
                    balle_venimeuse INT DEFAULT 0,
                    balle_electrique INT DEFAULT 0,
                    balle_gelante INT DEFAULT 0,
                    green_pop INT DEFAULT 0,
                    karate INT DEFAULT 0,
                    taekwondo INT DEFAULT 0,
                    judo INT DEFAULT 0,
                    boxe INT DEFAULT 0,
                    okama_kenpo INT DEFAULT 0,
                    hassoken INT DEFAULT 0,
                    ryusoken INT DEFAULT 0,
                    jambe_noire INT DEFAULT 0,
                    gyojin_karate_simplifie INT DEFAULT 0,
                    rope_action INT DEFAULT 0,
                    ramen_kenpo INT DEFAULT 0,
                    gyojin_karate INT DEFAULT 0,
                    art_martial_tontatta INT DEFAULT 0,
                    jao_kun_do INT DEFAULT 0,
                    electro INT DEFAULT 0,
                    sulong INT DEFAULT 0,
                    style_personnel INT DEFAULT 0,
                    FOREIGN KEY (user_id) REFERENCES user_stats (user_id)
                )''')
                await conn.commit()

        pool.close()
        await pool.wait_closed()
        logging.info("Base de données prête et tables créées.")

    except Exception as e:
        logging.error(f"Erreur lors de la connexion ou de la création des tables : {e}")


# Démarre le bot
bot.run('VOTRE_TOKEN')

    pool.close()
    await pool.wait_closed()

async def test_connection():
    # Informations de connexion
    host = "sql209.infinityfree.com"
    port = 3306
    user = "if0_38099598"
    password = "4bhv2sctOAw"
    db = "if0_38099598_bot_db"

    try:
        pool = await aiomysql.create_pool(
            host=host,
            port=port,
            user=user,
            password=password,
            db=db,
        )
        print("Connexion réussie à la base de données MySQL !")
    except Exception as e:
        print(f"Erreur lors de la connexion : {e}")

# Lancer l'événement loop
loop = asyncio.get_event_loop()
loop.run_until_complete(test_connection())

# Ajoutez vos autres commandes ou événements ici.


sabreur = {
    "Ittôryû": {
        "description": "Technique spéciale nécessitant l’usage d’un sabre. L'ittôryû est une compétence simple mais polyvalente, pouvant s’utiliser dans de nombreuses situations. Les techniques à un sabre sont des coups de lames renforcés, allant jusqu’à projeter des lames d’air tranchantes ou à trancher des matières solides comme du beurre. C’est une base primordiale pour les épéistes avant de créer leur style unique, ainsi que la source de nombreux dérivés."
    },
    "Nitôryû": {
        "description": "Dérivée de l'ittôryû, le style à deux sabres fonctionne de la même manière mais avec deux sabres pour des attaques offensives renforcées, allant jusqu'à de puissantes lames d’air. Ce style permet de combiner rapidité et puissance."
    },
    "Santôryû": {
        "description": "Le style du sabreur à trois sabres, généralement une limite technique pour la majorité des guerriers. Ceux qui maîtrisent ce style utilisent la troisième lame entre leurs dents, créant ainsi un style très agressif. Les attaques sont puissantes et peuvent créer des lames d’air distantes et puissantes. Toutefois, l’usage de ce style n’est pas recommandé pour une bonne hygiène dentaire."
    },
    "Mûtôryû": {
        "description": "Le style sans sabre, aussi appelé Mûtôryû, est assez particulier. Ce style ne renforce pas les lames, mais directement le corps de l’épéiste. Cela permet de créer des lames d’air avec des coups de bras ou d’autres parties du corps, imitant l’effet d’un sabre sans en posséder un."
    },
    "Style du Renard de Feu": {
        "description": "Développé à Wano Kuni, ce style flamboyant permet d'embraser sa lame et de trancher les flammes pour s’en protéger ou y créer des ouvertures. Bien que la création de flammes soit plus modeste que celle d’autres pouvoirs, ce style reste redoutable pour ses attaques offensives et sa capacité à se défendre contre le feu."
    },
    "Danse de l'Épée des Remous": {
        "description": "La danse de l’épée est une technique non-violente, visant à désarmer les adversaires plutôt qu’à les blesser. Le sabreur exécute une série de mouvements semblables à une danse, frappant les armes ennemies pour les faire tomber des mains de leurs porteurs."
    }
}

tireur = {
    "Style de Combat Tireur d'Élite": {
        "description": "Basé sur l’usage de projectiles et d’armes à feu, le tireur d’élite utilise des munitions spéciales modifiées pour s’adapter à toutes sortes de situations. Certaines de ces balles peuvent être renforcées par l’usage de Dials ou être personnalisées grâce à des techniques uniques. Les tireurs d’élite sont des experts dans l’usage des balles pour un maximum d’efficacité."
    },
    "Balle Explosive": {
        "description": "Balles couvertes ou contenant de la poudre à canon, ces balles explosent au contact d’une cible, provoquant des dégâts massifs à l'impact. Elles sont particulièrement efficaces contre les armures et les structures."
    },
    "Balle Incendiaire": {
        "description": "Ces balles s’enflamment par friction, créant une explosion de feu au moment du tir. Elles sont idéales pour enflammer une cible, déclencher des incendies ou brûler un adversaire sur place."
    },
    "Balle Fumigène": {
        "description": "Une balle contenant une poudre qui libère de la fumée au contact. Cela bloque la vue d’une ou plusieurs personnes, idéal pour aveugler un groupe d’adversaires ou créer des distractions. Cependant, elles sont vulnérables aux vents forts qui dispersent la fumée rapidement."
    },
    "Balle Dégoutante": {
        "description": "Plutôt que d'utiliser une balle classique, ce style utilise des projectiles répugnants : œufs pourris, balles recouvertes de crottes de pigeons, ou autres substances dégoûtantes. L’objectif est de perturber et de dégoûter l’adversaire, affectant souvent sa concentration ou son moral."
    },
    "Balle Cactus": {
        "description": "Au lieu d’une balle, un projectile à épines est lancé. Lorsqu’il explose, il libère plusieurs projectiles en forme de cactus, qui se plantent dans la peau de l’adversaire. Ces projectiles sont particulièrement douloureux et difficiles à enlever."
    },
    "Balle Venimeuse": {
        "description": "Ces balles contiennent des substances toxiques et dangereuses comme du poison ou des drogues. Elles peuvent affaiblir, empoisonner ou même tuer à petit feu l'adversaire si elles ne sont pas traitées à temps."
    },
    "Balle Électrique": {
        "description": "Les balles électriques fonctionnent comme un taser. Elles contiennent une petite batterie qui libère une décharge électrique au contact. Ces balles sont idéales pour paralyser une cible ou la neutraliser temporairement."
    },
    "Balle Gelante": {
        "description": "Ces balles contiennent de l'azote liquide ou d’autres substances permettant de geler instantanément la cible. Cela peut figer un membre ou même une partie du corps d’un ennemi, le rendant vulnérable aux attaques suivantes."
    },
    "Green Pop": {
        "description": "Ces balles contiennent des germes et des graines provenant du Nouveau Monde. Lorsqu’elles touchent une cible, elles germent et poussent en quelques secondes, créant des racines ou des plantes agressives. Ces plantes peuvent immobiliser, empoisonner ou causer des dommages physiques avec leurs épines et autres mécanismes."
    }
}

arts = {
    "Karaté": {
        "description": "Utilisant le corps de l’homme comme arme mêlant des mouvements offensifs comme défensifs tout en développant le bien-être de l’esprit."
    },
    "Taekwondo": {
        "description": "Style à percussion utilisant pieds et poings, le Taekwondo vise essentiellement entre la ceinture et le visage pour des coups impactants et rapides."
    },
    "Judo": {
        "description": "Le judo est un style de combat rapproché maximisant les contacts corporels pour projeter ou plaquer la cible au sol par l’usage de nombreuses prises utilisant l’entièreté du corps."
    },
    "Boxe": {
        "description": "Libre à nombreux dérivés, la boxe dans son état global consiste en un enchaînement de frappes puissantes vers le haut du corps et essentiellement le visage."
    }
}
  
combattant = {
    "Okama Kenpo": {
        "description": "Semblable à une danse de ballet, l’Okama Kenpo est un style reposant sur les coups de pieds et de jambes agiles, rapides et puissants. Une fois la fierté mise de côté, ce style est redoutable."
    },
    "Hassoken": {
        "description": "Art martial redoutablement fort originaire du pays des fleurs, le Hassoken est un style de combat brutal et impactant visant à créer des vibrations par les coups employés pour percer les défenses."
    },
    "Ryusoken": {
        "description": "Aussi appelé griffe du dragon, le Ryusoken est un art basé sur l’usage des mains comme des griffes de dragons pour écraser ses cibles avec une forte poigne, offrant une puissance destructrice à l’offensive, bien que difficile à diriger."
    },
    "Jambe noire": {
        "description": "Développé par des pirates cuisiniers, ce style permet de se battre en n’utilisant que ses jambes pour préserver l’état des mains. Ce style de coups de jambes permet une grande mobilité ainsi que des attaques destructrices et rapides. Maîtrisé à haut niveau, les experts peuvent faire usage du style de la Jambe du diable, une évolution de la jambe noire combinant la force des jambes avec une extrême chaleur corporelle, enflammant la jambe par la friction et la vitesse."
    },
    "Gyojin Karaté (simplifié)": {
        "description": "Adaptation du style des hommes poissons aux combattants terrestres, cette forme du Gyojin karaté permet des frappes offensives et défensives très puissantes."
    }
}

uniques = {
    "Rope Action": {
        "description": "Style de combat basé sur l’usage de câbles longs servant à l'attache des navires ou d’autres matériaux maritimes, visant à ligoter la cible avec puissance."
    },
    "Ramen Kenpo": {
        "description": "Utilisant nouilles et farine, le Ramen Kenpo est un art peu célèbre et complexe utilisant des nouilles pour se battre comme des armes ou comme armure. Pratique pour limiter les mouvements et immobiliser une cible, mais peu efficace face aux épéistes."
    },
    "Gyojin Karaté": {
        "description": "Style de combat similaire au karaté terrien, cet art utilise le corps de son utilisateur pour des mouvements de frappe offensifs comme défensifs. Au-delà de permettre aux hommes poissons des attaques puissantes et brutales, cet art permet aussi de manipuler l’eau environnante pour diriger des vagues ou des balles d’eau vers l'ennemi. Plus il y a d’eau à proximité, plus l’utilisateur sera redoutable, obtenant le plein potentiel de ce style lorsqu’il se bat en pleine mer."
    },
    "Art Martial Tontatta": {
        "description": "Basé sur l’usage de la force exceptionnelle de ces petits êtres, ce style offensif vise en premier temps à retirer ou arracher les vêtements de la cible pour la déconcentrer ou bien l'immobiliser avant de la frapper fort dans le but d’endormir ou de détruire."
    },
    "Jao Kun Do": {
        "description": "Ce style utilise les jambes étirées des longues jambes pour frapper avec la force de l’acier et maintenir l’adversaire à une certaine distance tout en attaquant. Mobile et puissant, ce n’est pas un style à sous-estimer."
    },
    "Electro": {
        "description": "Comme son nom l’indique, il s’agit ici d’une technique offensive visant à libérer de l’électricité sur l’adversaire grâce à la constitution biologique étrange des Minks, capables de produire facilement de l’électricité. Tous les Minks en sont capables, même les plus jeunes."
    },
    "Sulong": {
        "description": "Sous la lueur d’une pleine lune, les Minks les plus puissants obtiennent une nouvelle forme aussi imposante que destructrice. Sous cette forme, les yeux de l'individu changent, ses poils poussent énormément en prenant une couleur blanche, mais surtout leurs tailles et toutes leurs compétences physiques augmentent radicalement. Cependant, sous cette forme, la raison est mise de côté, laissant les individus se faire guider par l’instinct sauvage."
    }
}

perso = {
    "Style Personnel": {
        "description": "Pirates libres comme l’air ou marines et révolutionnaires voulant se démarquer des autres, il est normal d’avoir envie de créer un style de combat unique à soi-même, un art adapté parfaitement à nos compétences et nos besoins. Cela est possible, que ce soit en partant de rien ou en se basant sur d’autres styles de combats, mais cela demande de l'intelligence et de l’entraînement ! Pour ce faire, il faudra simplement voir les membres du staff en ticket et leur présenter sous une fiche votre style."
    }
}

# Dictionnaires des techniques pour chaque catégorie
skills_liste = {
    "Sabreur": sabreur,
    "Tireur": tireur,
    "Arts Martiaux": arts,
    "Combattant": combattant,
    "Uniques": uniques,
    "Personnel": perso
}

# Localisation du fichier de base de données
db_file = '/workspace/inventory.db'
backup_file = '/workspace/inventory_backup.db'

# Copier le fichier vers un fichier de sauvegarde
shutil.copy(db_file, backup_file)

# Si tu veux compresser ce fichier en .zip
shutil.make_archive('/workspace/inventory_backup', 'zip', '/workspace', 'inventory.db')

print(f"Backup créé : /workspace/inventory_backup.zip")

@bot.command()
async def setup(ctx, user: discord.User):
    # Vérifie si l'utilisateur a le rôle de staff (modérateur ou administrateur)
    if not any(role.id in STAFF_ROLES_IDS for role in ctx.author.roles):
        await ctx.send("Tu n'as pas les permissions nécessaires pour utiliser cette commande.")
        return

    # Récupérer l'ID de l'utilisateur mentionné
    user_id = user.id

    retries = 3  # Nombre de tentatives en cas de verrouillage
    for attempt in range(retries):
        try:
            # Connexion à la base de données avec gestion du verrouillage
            async with aiosqlite.connect('inventory.db') as db:
                # Liste des catégories de techniques
                categories = ["Sabreur", "Tireur", "Arts Martiaux", "Combattant", "Uniques", "Personnel"]

                for category in categories:
                    # Récupérer toutes les techniques pour cette catégorie
                    skills = skills_liste.get(category)
                    if skills:
                        for skill_name in skills:
                            # Vérifie si la technique existe pour l'utilisateur
                            cursor = await db.execute('SELECT palier FROM skills_stats WHERE user_id = ? AND skills_name = ?', (user_id, skill_name))
                            skill = await cursor.fetchone()

                            if not skill:
                                # Si la technique n'existe pas pour l'utilisateur, on l'ajoute avec palier 0
                                await db.execute('INSERT INTO skills_stats (user_id, skills_name, palier) VALUES (?, ?, ?)', (user_id, skill_name, 0))
                            else:
                                # Sinon, on met simplement le palier à 0
                                await db.execute('UPDATE skills_stats SET palier = 0 WHERE user_id = ? AND skills_name = ?', (user_id, skill_name))

                await db.commit()
            await ctx.send(f"Toutes les techniques de {user.name} ont été initialisées à palier 0.")
            return  # Si l'opération est réussie, on sort de la boucle

        except aiosqlite.DatabaseError as e:
            if attempt < retries - 1:
                await asyncio.sleep(2)  # Attendre 2 secondes avant de réessayer
                continue  # Réessayer l'opération
            else:
                await ctx.send("Une erreur est survenue en accédant à la base de données, essaye de réessayer plus tard.")
                print(f"Erreur de base de données: {e}")
                return

@bot.command(name='edit')
async def edit(ctx, edit_type: str, value: str):
    # Vérification du type d'édition
    if edit_type not in ["thumbnail", "icon", "main", "color", "ost"]:
        await ctx.send("Veuillez spécifier le type à éditer: `thumbnail`, `icon`, `main`, `color` ou `ost`.")
        return

    # Validation de l'URL ou couleur
    if edit_type in ["thumbnail", "icon", "main", "ost"]:
        if not (value.startswith("http://") or value.startswith("https://")):
            await ctx.send("Veuillez fournir une URL valide.")
            return
    if edit_type == "color":
        if not (value.startswith("#") and len(value) in [4, 7]):
            await ctx.send("Veuillez fournir une couleur valide au format HEX (par exemple, `#FFBF66`).")
            return
    if edit_type == "ost":
        if "youtube.com" not in value and "youtu.be" not in value:
            await ctx.send("Veuillez fournir une URL YouTube valide pour l'OST.")
            return

    # Choix de la colonne en fonction du type
    column = {
        "thumbnail": "thumbnail_url",
        "icon": "icon_url",
        "main": "main_url",
        "color": "color",
        "ost": "ost_url"
    }[edit_type]

    async with aiosqlite.connect('inventory.db') as db:
        try:
            # Mise à jour ou insertion des personnalisations
            await db.execute(f'''
                INSERT INTO user_decorations (user_id, {column})
                VALUES (?, ?)
                ON CONFLICT(user_id) DO UPDATE SET {column} = excluded.{column}
            ''', (ctx.author.id, value))
            await db.commit()
            await ctx.send(f"{edit_type.capitalize()} mis à jour avec succès ! Elle apparaîtra dans votre commande `?stats`.")
        except Exception as e:
            logging.error(f"Erreur lors de la mise à jour de {edit_type} pour l'utilisateur {ctx.author.id}: {e}")
            await ctx.send("Une erreur est survenue lors de la mise à jour.")

@bot.command(name='stats')
async def stats(ctx, member: discord.Member = None):
    target_member = member or ctx.author
    logging.info(f"Fetching stats for user: {target_member.id}")

    async with aiosqlite.connect('inventory.db') as db:
        try:
            async with db.execute('SELECT * FROM user_stats WHERE user_id = ?', (target_member.id,)) as cursor:
                stats = await cursor.fetchone()

            if not stats:
                logging.debug(f"Aucune stats trouvée pour l'utilisateur {target_member.id}. Création d'une nouvelle entrée.")
                await db.execute('INSERT INTO user_stats (user_id) VALUES (?)', (target_member.id,))
                await db.commit()
                stats = (target_member.id, 5, 5, 5, 5, 5, 5, 0, 0, 0, 0, 0, 0)

            (user_id, force, vitesse, resistance, endurance, agilite, combat, FDD, haki_armement, haki_observation, haki_rois, points, points_spent) = stats

            async with db.execute('SELECT thumbnail_url, icon_url, main_url, color, ost_url FROM user_decorations WHERE user_id = ?', (target_member.id,)) as cursor:
                decorations = await cursor.fetchone()

            if decorations:
                thumbnail_url, icon_url, main_url, color_hex, ost_url = decorations
                # Convertit la couleur en entier si elle est fournie sous forme hexadécimale
                color = int(color_hex.lstrip('#'), 16) if color_hex else 0xFFBF66
            else:
                thumbnail_url, icon_url, main_url, color, ost_url = (None, None, None, 0xFFBF66, None)

            embed = discord.Embed(
                title=f"Statistiques de {target_member.display_name}", 
                color=color,
                description=(
                    f"**Points disponibles : {points}**\n"
                    f"**Elo : {points_spent}**\n\n"
                    f"**╔═══════════ ∘◦ ✾ ◦∘ ════════════╗**\n\n"
                    f"**💪 ・ Force**: ➠ {force}%\n"
                    f"**🦵 ・ Vitesse**: ➠ {vitesse}%\n"
                    f"**🛡️ ・ Résistance**: ➠ {resistance}%\n"
                    f"**🫁 ・ Endurance**: ➠ {endurance}%\n"
                    f"**🤸‍♂️ ・ Agilité**: ➠ {agilite}%\n\n"
                    f"**════════════ ∘◦ ⛧ﾐ ◦∘ ════════════**\n\n"
                    f"**🥊 ・ Maîtrise de combat**: ➠ {combat}%\n"
                    f"**🍇 ・ Maîtrise de Fruit du démon**: ➠ {FDD}%\n\n"
                    f"**════════════ ∘◦ ⛧ﾐ ◦∘ ════════════**\n\n"
                    f"**🦾 ・ Haki de l'armement**: ➠ {haki_armement}%\n"
                    f"**👁️ ・ Haki de l'observation**: ➠ {haki_observation}%\n"
                    f"**👑 ・ Haki des Rois**: ➠ {haki_rois}%\n\n"
                    f"**╚═══════════ ∘◦ ❈ ◦∘ ════════════╝**"
                )
            )

            if thumbnail_url:
                embed.set_thumbnail(url=thumbnail_url)
            if icon_url:
                embed.set_author(name=target_member.display_name, icon_url=icon_url)
            if main_url:
                embed.set_image(url=main_url)
            if ost_url:
                embed.add_field(name="OST", value=f"[Cliquez ici pour écouter]({ost_url})", inline=False)

            await ctx.send(embed=embed)
        except Exception as e:
            logging.error(f"Erreur lors de la récupération des stats: {e}")
            await ctx.send("Une erreur est survenue lors de la récupération des statistiques.")
        
train_cooldown = datetime.timedelta(hours=24)  # Cooldown de 24 heures
user_last_train = {}  # Dictionnaire pour stocker les derniers entraînements des utilisateurs

@bot.command(name='train')
async def train(ctx):
    fiche_role = discord.utils.get(ctx.author.roles, id=1270083788529074220)
    
    if not fiche_role:
        embed = discord.Embed(
            title="Fiche non validée",
            description="Vous ne pouvez pas entraîner car votre fiche n'a pas encore été validée.",
            color=0xFF0000
        )
        await ctx.send(embed=embed)
        return

    current_time = datetime.datetime.now()
    last_train_time = user_last_train.get(ctx.author.id, datetime.datetime.fromtimestamp(0))

    if current_time - last_train_time < train_cooldown:
        remaining_time = train_cooldown - (current_time - last_train_time)
        hours, remainder = divmod(remaining_time.total_seconds(), 3600)
        minutes, _ = divmod(remainder, 60)
        time_left = f"{int(hours)} heures et {int(minutes)} minutes"
        
        embed = discord.Embed(
            title="Temps de cooldown",
            description=f"Vous devez attendre encore **{time_left}** avant de pouvoir entraîner cette capacité à nouveau.",
            color=0xFF0000
        )
        await ctx.send(embed=embed)
        return

    await ctx.send("Écrivez un message pour l'entraînement (minimum 150 caractères)")

    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel

    try:
        message = await bot.wait_for('message', check=check, timeout=300)  # 5 minutes pour répondre
    except asyncio.TimeoutError:
        await ctx.send("Vous n'avez pas répondu à temps.")
        return

    message_length = len(message.content)
    
    # Vérification du minimum de 150 caractères
    if message_length < 150:
        await ctx.send("Votre message doit contenir au moins 150 caractères pour valider l'entraînement.")
        return
    
    # Points en fonction de la longueur du message
    if message_length < 500:
        points_gagnes = random.choice([4, 5])
    elif 500 <= message_length <= 1000:
        points_gagnes = random.choice([5, 6])
    else:
        points_gagnes = random.choice([6, 7])
    
    # Ajout d'un point pour les boosters
    booster_role = discord.utils.get(ctx.guild.roles, id=1286757193651322971)
    if booster_role in ctx.author.roles:
        points_gagnes += 1

    # Sauvegarder les points gagnés
    async with aiosqlite.connect('inventory.db') as db:
        async with db.execute('SELECT points FROM user_stats WHERE user_id = ?', (ctx.author.id,)) as cursor:
            result = await cursor.fetchone()
            current_points = result[0] if result else 0

        new_points = current_points + points_gagnes
        await db.execute('UPDATE user_stats SET points = ? WHERE user_id = ?', (new_points, ctx.author.id))
        await db.commit()

    user_last_train[ctx.author.id] = current_time

    embed = discord.Embed(
        title="Entraînement terminé",
        description=f"Vous avez gagné {points_gagnes} points d'entraînement.",
        color=0xFFBF66
    )
    await ctx.send(embed=embed)


@bot.command(name='points')
async def points(ctx, action: str, amount: int, member: discord.Member = None):
    allowed_role_ids = [1269837965446610985, 1269838005234044958]  # Remplace par l'ID correct

    # Vérification si l'utilisateur possède le rôle admin
    admin_role = discord.utils.get(ctx.author.roles, id=allowed_role_ids)
    if not any(role.id in allowed_role_ids for role in ctx.author.roles):
        await ctx.send("Vous n'avez pas la permission d'utiliser cette commande.")
        return

    if action not in ['add', 'remove']:
        await ctx.send("Utilisez `add` pour ajouter des points ou `remove` pour en retirer.")
        return

    if amount <= 0:
        await ctx.send("La quantité de points doit être positive.")
        return

    member = member or ctx.author

    async with aiosqlite.connect('inventory.db') as db:
        async with db.execute('SELECT points FROM user_stats WHERE user_id = ?', (member.id,)) as cursor:
            result = await cursor.fetchone()
            current_points = result[0] if result else 0

        if action == 'add':
            new_points = current_points + amount
        elif action == 'remove':
            new_points = max(0, current_points - amount)

        await db.execute('UPDATE user_stats SET points = ? WHERE user_id = ?', (new_points, member.id))
        await db.commit()

        embed = discord.Embed(
        title="Points mis à jour",
        description=f"{amount} points {action}. Les points de {member.mention} sont déormais à {new_points} .",
        color=0xFFBF66
        )
        await ctx.send(embed=embed)

@bot.command(name='elo')
async def points(ctx, action: str, amount: int, member: discord.Member = None):
    allowed_role_ids = [1269837965446610985, 1269838005234044958]  # Remplace par l'ID correct

    # Vérification si l'utilisateur possède le rôle admin
    admin_role = discord.utils.get(ctx.author.roles, id=allowed_role_ids)
    if not any(role.id in allowed_role_ids for role in ctx.author.roles):
        await ctx.send("Vous n'avez pas la permission d'utiliser cette commande.")
        return

    if action not in ['add', 'remove']:
        await ctx.send("Utilisez `add` pour ajouter des points ou `remove` pour en retirer.")
        return

    if amount <= 0:
        await ctx.send("La quantité de points d'Elo doit être positive.")
        return

    member = member or ctx.author

    async with aiosqlite.connect('inventory.db') as db:
        async with db.execute('SELECT points_spent FROM user_stats WHERE user_id = ?', (member.id,)) as cursor:
            result = await cursor.fetchone()
            current_points = result[0] if result else 0

        if action == 'add':
            new_points = current_points + amount
        elif action == 'remove':
            new_points = max(0, current_points - amount)

        await db.execute('UPDATE user_stats SET points_spent = ? WHERE user_id = ?', (new_points, member.id))
        await db.commit()

        embed = discord.Embed(
        title="Points mis à jour",
        description=f"{amount} Elo {action}. L'Elo de {member.mention} est déormais à {new_points} .",
        color=0xFFBF66
        )
        await ctx.send(embed=embed)


@bot.command(name="upgrade")
async def upgrade(ctx):
    async with aiosqlite.connect('inventory.db') as db:
        # Récupérer les statistiques actuelles et les points disponibles
        async with db.execute('SELECT points, points_spent, force, resistance, endurance, vitesse, agilite, combat, FDD, haki_armement, haki_observation, haki_rois FROM user_stats WHERE user_id = ?', (ctx.author.id,)) as cursor:
            result = await cursor.fetchone()

        if result is None:
            await ctx.send("Aucune donnée trouvée pour cet utilisateur.")
            return

        points, points_spent, force, resistance, endurance, vitesse, agilite, combat, FDD, haki_armement, haki_observation, haki_rois = result

        # Récupérer les rôles de l'utilisateur pour vérifier le rôle FDD
        fdd_role_id = 1269823257079447623  # Remplacez par l'ID réel du rôle FDD
        hda_role_id = 1269823110958415934  # Remplacez par l'ID réel du rôle HDA
        hdo_role_id = 1269823083519279155  # Remplacez par l'ID réel du rôle HDO
        hdr_role_id = 1269823037830856744  # Remplacez par l'ID réel du rôle HDR

        has_fdd_role = discord.utils.get(ctx.author.roles, id=fdd_role_id) is not None
        has_hda_role = discord.utils.get(ctx.author.roles, id=hda_role_id) is not None
        has_hdo_role = discord.utils.get(ctx.author.roles, id=hdo_role_id) is not None
        has_hdr_role = discord.utils.get(ctx.author.roles, id=hdr_role_id) is not None


        # Création du menu déroulant
        select = Select(
            placeholder="Choisissez une statistique à améliorer...",
            options=[
                SelectOption(label="💪 Force", description=f"Améliorer Force (Actuel: {force}%)"),
                SelectOption(label="🛡️ Résistance", description=f"Améliorer Résistance (Actuel: {resistance}%)"),
                SelectOption(label="🫁 Endurance", description=f"Améliorer Endurance (Actuel: {endurance}%)"),
                SelectOption(label="🦵 Vitesse", description=f"Améliorer Vitesse (Actuel: {vitesse}%)"),
                SelectOption(label="🤸‍♂️ Agilité", description=f"Améliorer Agilité (Actuel: {agilite}%)"),
                SelectOption(label="🥊 Combat", description=f"Améliorer Combat (Actuel: {combat}%)"),
                SelectOption(label="🍇 FDD", description=f"Améliorer FDD (Actuel: {FDD}%)"),
                SelectOption(label="🦾 HDA", description=f"Débloquer/Améliorer HDA (Actuel: {haki_armement}%)"),
                SelectOption(label="👁️ HDO", description=f"Débloquer/Améliorer HDO (Actuel: {haki_observation}%)"),
                SelectOption(label="👑 HDR", description=f"Débloquer/Améliorer HDR (Actuel: {haki_rois}%)"),
            ]
        )

        async def select_callback(interaction):
            async with aiosqlite.connect('inventory.db') as db:
                # Mettre à jour les points et statistiques avant chaque interaction
                async with db.execute('SELECT points, points_spent, force, resistance, endurance, vitesse, agilite, combat, FDD, haki_armement, haki_observation, haki_rois FROM user_stats WHERE user_id = ?', (ctx.author.id,)) as cursor:
                    updated_result = await cursor.fetchone()

                points, points_spent, force, resistance, endurance, vitesse, agilite, combat, FDD, haki_armement, haki_observation, haki_rois = updated_result

                chosen_stat = select.values[0]

                stat_map = {
                    "💪 Force": "force",
                    "🛡️ Résistance": "resistance",
                    "🫁 Endurance": "endurance",
                    "🦵 Vitesse": "vitesse",
                    "🤸‍♂️ Agilité": "agilite",
                    "🥊 Combat": "combat",
                    "🍇 FDD": "FDD",
                    "🦾 HDA": "haki_armement",
                    "👁️ HDO": "haki_observation",
                    "👑 HDR": "haki_rois"
                }

                stat_col = stat_map.get(chosen_stat)

                if not stat_col:
                    embed = Embed(
                        title="Erreur",
                        description="Statistique sélectionnée invalide.",
                        color=0xFFBF66
                    )
                    await interaction.response.send_message(embed=embed)
                    return

                # Vérifier les conditions Elo pour Haki et FDD
                if stat_col == "haki_armement" and not (points_spent >= 500 or has_hda_role and points_spent >= 250):
                    embed = Embed(
                        title="Condition non remplie",
                        description="Vous devez avoir 500 Elo ou le rôle HDA et minimum 250 Elo pour améliorer Haki de l'Armement.",
                        color=0xFFBF66
                    )
                    await interaction.response.send_message(embed=embed)
                    return
                elif stat_col == "haki_observation" and not (points_spent >= 500 or has_hdo_role and points_spent >= 250):
                    embed = Embed(
                        title="Condition non remplie",
                        description="Vous devez avoir 500 Elo ou le rôle HDO et minimum 250 Elo pour améliorer Haki de l'Observation.",
                        color=0xFFBF66
                    )
                    await interaction.response.send_message(embed=embed)
                    return
                elif stat_col == "haki_rois" and not (points_spent >= 1000 or has_hdr_role and points_spent >= 500):
                    embed = Embed(
                        title="Condition non remplie",
                        description="Vous avez besoin d'au moins 1000 Elo ou le rôle HDR et 500 Elo pour améliorer Haki des Rois.",
                        color=0xFFBF66
                    )
                    await interaction.response.send_message(embed=embed)
                    return
                elif stat_col == "FDD" and not has_fdd_role:
                    embed = Embed(
                        title="Condition non remplie",
                        description="Vous avez besoin du rôle FDD pour améliorer cette statistique.",
                        color=0xFFBF66
                    )
                    await interaction.response.send_message(embed=embed)
                    return

                # Récupérer la valeur actuelle de la statistique choisie
                stats = {
                    "force": force,
                    "resistance": resistance,
                    "endurance": endurance,
                    "vitesse": vitesse,
                    "agilite": agilite,
                    "combat": combat,
                    "FDD": FDD,
                    "haki_armement": haki_armement,
                    "haki_observation": haki_observation,
                    "haki_rois": haki_rois
                }

                current_stat = stats.get(stat_col)

                if current_stat is None:
                    embed = Embed(
                        title="Erreur",
                        description="Erreur de récupération des données.",
                        color=0xFFBF66
                    )
                    await interaction.response.send_message(embed=embed)
                    return

                # Calcul des points requis
                if current_stat < 50:
                    points_needed = 4 if stat_col in ["force", "resistance", "endurance", "vitesse", "agilite"] else 10 if stat_col in ["combat", "FDD"] else 14 if stat_col in ["haki_armement", "haki_observation"] else 18
                elif current_stat < 100:
                    points_needed = 6 if stat_col in ["force", "resistance", "endurance", "vitesse", "agilite"] else 12 if stat_col in ["combat", "FDD"] else 16 if stat_col in ["haki_armement", "haki_observation"] else 20
                elif current_stat < 150:
                    points_needed = 8 if stat_col in ["force", "resistance", "endurance", "vitesse", "agilite"] else 14 if stat_col in ["combat", "FDD"] else 18 if stat_col in ["haki_armement", "haki_observation"] else 22
                else:
                    points_needed = 10 if stat_col in ["force", "resistance", "endurance", "vitesse", "agilite"] else 16 if stat_col in ["combat", "FDD"] else 20 if stat_col in ["haki_armement", "haki_observation"] else 25

                # Vérification des points
                if points >= points_needed:
                    # Mise à jour de la statistique
                    new_stat = current_stat + 5
                    update_query = f"UPDATE user_stats SET {stat_col} = ? WHERE user_id = ?"
                    await db.execute(update_query, (new_stat, ctx.author.id))
                    await db.commit()

                    # Mise à jour des points
                    new_points = points - points_needed
                    await db.execute("UPDATE user_stats SET points = ?, points_spent = ? WHERE user_id = ?", (new_points, points_spent + points_needed, ctx.author.id))
                    await db.commit()

                    # Envoi du message de confirmation
                    embed = Embed(
                        title="Amélioration réussie",
                        description=f"Votre {chosen_stat} est maintenant à {new_stat}%. Il vous reste {new_points} points.",
                        color=0xFFBF66
                    )
                    await interaction.response.send_message(embed=embed)
                else:
                    embed = Embed(
                        title="Points insuffisants",
                        description=f"Vous avez besoin de {points_needed} points pour améliorer cette statistique.",
                        color=0xFFBF66
                    )
                    await interaction.response.send_message(embed=embed)

        select.callback = select_callback
        view = View()
        view.add_item(select)


        # Envoyer le menu déroulant avec embed
        embed = Embed(
            title="Amélioration des Statistiques",
            description=f"Vous avez actuellement **{points} points** et **{points_spent} Elo**. Choisissez une statistique à améliorer :",
            color=0xFFBF66
        )
        await ctx.send(embed=embed, view=view)

@bot.command(name="nerf")
async def nerf(ctx, stat: str, percentage: int, member: discord.Member):
    allowed_role_ids = [1269837965446610985, 1269838005234044958]  # Remplace par l'ID correct
    # Vérification si l'utilisateur possède le rôle admin
    admin_role = discord.utils.get(ctx.author.roles, id=allowed_role_ids)
    if not any(role.id in allowed_role_ids for role in ctx.author.roles):
        await ctx.send("Vous n'avez pas la permission d'utiliser cette commande.")
        return
    
    if stat.lower() not in ["force", "resistance", "endurance", "vitesse", "agilite", "combat", "FDD", "haki_armement", "haki_observation", "haki_rois"]:
        await ctx.send(f"La statistique '{stat}' est invalide.")
        return

    async with aiosqlite.connect('inventory.db') as db:
        async with db.execute(f'SELECT {stat.lower()} FROM user_stats WHERE user_id = ?', (member.id,)) as cursor:
            result = await cursor.fetchone()

        if result is None:
            await ctx.send(f"Aucune donnée trouvée pour l'utilisateur {member.display_name}.")
            return

        current_value = result[0]

        # Calcul du nouveau pourcentage
        new_value = max(0, current_value - percentage)

        # Mise à jour de la statistique dans la base de données
        await db.execute(f'UPDATE user_stats SET {stat.lower()} = ? WHERE user_id = ?', (new_value, member.id))
        await db.commit()

    await ctx.send(f"La statistique **{stat}** de {member.mention} a été réduite de {percentage}%. Elle est maintenant à {new_value}%.")


@bot.command(name="top")
async def top(ctx, page: int = 1):
    fiche_role_id = 1270083788529074220  # Remplace avec l'ID réel du rôle Fiche validée
    print("Commande ?top déclenchée.")
    
    role_fiche = discord.utils.get(ctx.guild.roles, id=fiche_role_id)
    if role_fiche is None:
        print("Le rôle Fiche validée est introuvable.")
        await ctx.send("Le rôle Fiche validée n'existe pas sur ce serveur.")
        return
    
    print("Rôle Fiche validée trouvé.")
    
    # Connexion à la base de données
    async with aiosqlite.connect('inventory.db') as db:
        print("Connexion à la base de données réussie.")
        async with db.execute('''
            SELECT user_id, points_spent
            FROM user_stats
            ORDER BY points_spent DESC
        ''') as cursor:
            all_users = await cursor.fetchall()
            print(f"Nombre d'utilisateurs récupérés depuis la base de données : {len(all_users)}")

    # Récupérer directement les membres ayant le rôle "Fiche validée"
    valid_users = []
    for user_id, points_spent in all_users:
        try:
            member = await ctx.guild.fetch_member(user_id)  # Récupérer directement le membre depuis l'API
            if role_fiche in member.roles:
                print(f"L'utilisateur {member.display_name} a le rôle Fiche validée.")
                valid_users.append((member, points_spent))
            else:
                print(f"L'utilisateur {member.display_name} n'a pas le rôle Fiche validée.")
        except discord.NotFound:
            print(f"Utilisateur introuvable : {user_id}")
        except discord.Forbidden:
            print(f"Accès refusé pour l'utilisateur : {user_id}")

    print(f"Nombre d'utilisateurs avec le rôle Fiche validée : {len(valid_users)}")
    
    if not valid_users:
        await ctx.send("Aucun utilisateur avec le rôle Fiche validée n'a été trouvé.")
        return

    # Pagination (10 utilisateurs par page)
    users_per_page = 10
    total_pages = (len(valid_users) - 1) // users_per_page + 1
    print(f"Total de pages : {total_pages}")

    if page < 1 or page > total_pages:
        print(f"Page {page} invalide.")
        await ctx.send(f"Page invalide. Veuillez entrer un nombre de page entre 1 et {total_pages}.")
        return

    start_index = (page - 1) * users_per_page
    end_index = start_index + users_per_page
    users_on_page = valid_users[start_index:end_index]

    # Créer l'embed de classement
    embed = discord.Embed(title=f"Classement Elo (Page {page}/{total_pages})", color=0xFFBF66)
    for rank, (member, points_spent) in enumerate(users_on_page, start=start_index + 1):
        embed.add_field(name=f"{rank}/ {member.display_name}", value=f"***{elo_emoji} Elo: {points_spent} \n\n***", inline=False)
    
    print(f"Affichage des utilisateurs sur la page {page}.")
    
    # Ajouter une note pour la pagination
    embed.set_footer(text=f"Page {page}/{total_pages} • Utilisez ?top <numéro de page> pour naviguer.")

    await ctx.send(embed=embed)
    print("Classement envoyé.")



@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Désolé, cette commande n'existe pas. Veuillez vérifier la commande et réessayer.")
            


@bot.command()
async def pong(ctx):
    await ctx.send("Ping!")
    print('Commande fonctionnelle !')


@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")


@bot.command()
async def Sinfos(ctx):
    server = ctx.guild
    serveurName = server.name
    numberOfTextChannels = len(server.text_channels)
    numberOfVoiceChannels = len(server.voice_channels)
    numberOfMembers = server.member_count
    owner = server.owner
    serveurRoles = server.roles
    embed = discord.Embed(title = "Serveur Informations", description= "Informations du serveur !", color=0xFFBF66)
    embed.add_field(name = "*Nom du serveur*", value = serveurName, inline=True)
    embed.add_field(name = "*Propriétaire*", value = owner, inline=True)
    embed.add_field(name = "*Membres*", value = numberOfMembers, inline=False)
    embed.add_field(name = "*Salons textuels*", value = numberOfTextChannels, inline=True)
    embed.add_field(name = "*Salons vocaux*", value = numberOfVoiceChannels, inline=True)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1269063423535222858/1269168943898296432/photo-by-patrick-on-unsplash-1649426391.jpg?ex=66af1530&is=66adc3b0&hm=3dfbddd2c6ce8db0c90e8ed88bcd90cef55b146eedaa936be86637e578cb6500&")
    await ctx.send(embed = embed)


@bot.command()
async def say(ctx, *texte):
    await ctx.send(" ".join(texte))

welcome_channel = 1269309406391042145

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(welcome_channel)
    if channel is not None:
        new_member = f"Bienvenue à {member.mention} sur le serveur, nous te souhaitons tous une bonne aventure sur les mers !"
        embed = discord.Embed(
            title="Nouvel arrivant !",
            description=new_member,
            color=0xFFBF66,
            timestamp=datetime.datetime.utcnow()
        )
        
        embed.set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
        embed.set_image(url="https://media1.tenor.com/m/o0NOobSt-AwAAAAC/luffy-gear-5.gif")
        embed.set_footer(text="Nous sommes ravis de vous accueillir !")

        await channel.send(embed=embed)


@bot.command()
@commands.has_permissions(manage_messages=True)  # Assurez-vous que l'utilisateur a la permission de gérer les messages
    
async def clear(ctx, amount: int):
    """Supprime un nombre spécifié de messages du canal actuel, en ignorant les messages du bot."""
    embed_error = discord.Embed(title="Commande invalide", color=0xFFBF66, description="Le nombre de messages à supprimer doit être supérieur à 0.")
    if amount <= 0:
        await ctx.send(embed = embed_error)
        return

    def is_not_bot(message):
        return not message.author.bot

    # Récupérer les messages à supprimer, en excluant ceux du bot
    
    await ctx.channel.purge(limit=amount+1, check=is_not_bot)
    deleted_message = f"{amount} messages supprimés."
    embed_clear = discord.Embed(title="Clear Messages", color=0xFFBF66, description=deleted_message)

    await ctx.send(embed = embed_clear, delete_after=5)
    
@clear.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        embed = discord.Embed(title="Erreur dans la commande", color=0xFFBF66, description="Vous n'avez pas la permission de gérer les messages.")
        await ctx.send(embed = embed)

zoan_classique = {
    "Inu Inu no Mi modèle Loup": {
        "description": "Permet à son utilisateur de devenir entièrement ou partiellement un loup.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Hito Hito no Mi": {
        "description": "Permet à son utilisateur (si animal) de devenir entièrement ou partiellement humain. Si un homme le mange il sera apparemment “éclairé.”",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Mogu Mogu no Mi": {
        "description": "Permet à son utilisateur de devenir entièrement ou partiellement une taupe.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Uma Uma no Mi": {
        "description": "Permet à son utilisateur de devenir entièrement ou partiellement un cheval.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Uma Uma no Mi modèle Zèbre": {
        "description": "Permet à son utilisateur de devenir entièrement ou partiellement un zèbre.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Zo Zo no Mi": {
        "description": "Permet à son utilisateur de devenir entièrement ou partiellement un éléphant.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Kawa Kawa no Mi": {
        "description": "Permet à son utilisateur de devenir entièrement ou partiellement une loutre de mer.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Sara Sara no Mi": {
        "description": "Permet à son utilisateur de devenir entièrement ou partiellement un axolotl.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Koara Koara no Mi": {
        "description": "Permet à son utilisateur de devenir entièrement ou partiellement un koala.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Kame Kame no Mi": {
        "description": "Permet à son utilisateur de devenir entièrement ou partiellement une tortue terrestre.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Neko Neko no Mi modèle Tigre": {
        "description": "Permet à son utilisateur de devenir entièrement ou partiellement un tigre.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Neko Neko no Mi modèle Guépard": {
        "description": "Permet à son utilisateur de devenir entièrement ou partiellement un guépard.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Rama Rama no Mi": {
        "description": "Permet à son utilisateur de devenir entièrement ou partiellement un lama.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Rama Rama no Mi": {
        "description": "Permet à son utilisateur de devenir entièrement ou partiellement un lama.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Ushi Ushi no mi modèle Bison": {
        "description": "Permet à son utilisateur de devenir entièrement ou partiellement un bison.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Ushi Ushi no mi modèle Girafe": {
        "description": "Permet à son utilisateur de devenir entièrement ou partiellement une girafe.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Ushi Ushi no mi modèle Rhinocéros": {
        "description": "Permet à son utilisateur de devenir entièrement ou partiellement un Rhinocéros.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Ushi Ushi no mi modèle taureau (minotaure)": {
        "description": "Permet à son utilisateur de devenir entièrement ou partiellement un taureau.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Inu Inu no mi modèle Basset": {
        "description": "Permet à son utilisateur de devenir entièrement ou partiellement un canidé, plus précisément un Basset.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Inu Inu no mi modèle Chacal": {
        "description": "Permet à son utilisateur de devenir entièrement ou partiellement un canidé, plus précisément un chacal.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Inu Inu no mi modèle Loup": {
        "description": "Permet à son utilisateur de devenir entièrement ou partiellement un loup.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Inu Inu no mi modèle Dalmatien": {
        "description": "Permet à son utilisateur de devenir entièrement ou partiellement un chien de la race dalmatien.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Inu Inu no mi modèle Chihuahua": {
        "description": "Permet à son utilisateur de devenir entièrement ou partiellement un chien de la race Chihuahua.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Inu Inu no mi modèle Tanuki": {
        "description": "Permet à son utilisateur de devenir entièrement ou partiellement un tanuki.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Tori Tori no mi modèle Aigle": {
        "description": "Permet à son utilisateur de devenir entièrement ou partiellement un aigle.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Tori Tori no mi modèle Faucon": {
        "description": "Permet à son utilisateur de devenir entièrement ou partiellement un faucon.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Tori Tori no mi modèle Albatros": {
        "description": "Permet à son utilisateur de devenir entièrement ou partiellement un albatros.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Tama Tama no mi": {
        "description": "Permet à son utilisateur de devenir entièrement ou partiellement un œuf.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Hebi Hebi no mi modèle Anaconda": {
        "description": "Permet à son utilisateur de devenir entièrement ou partiellement un anaconda.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Hebi Hebi no mi modèle Cobra royal": {
        "description": "Permet à son utilisateur de devenir entièrement ou partiellement un cobra royal.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Kumo Kumo no mi (Onigumo)": {
        "description": "Permet à son utilisateur de devenir entièrement ou partiellement un cobra araignée.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Mushi Mushi no mi modèle Scarabée Rhinocéros": {
        "description": "Permet à son utilisateur de devenir entièrement ou partiellement un scarabée rhinocéros.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Mushi Mushi no mi modèle Abeille": {
        "description": "Permet à son utilisateur de devenir entièrement ou partiellement une abeille.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Mushi Mushi no mi modèle Chenille": {
        "description": "Permet à son utilisateur de devenir entièrement ou partiellement une chenille.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    }

    
}

zoan_antique = {
    "Neko Neko no mi modèle Tigre à dents de sabre": {
        "description": "Permet à son utilisateur de devenir entièrement ou partiellement un Tigre à dents de sabre.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Kumo Kumo no mi modèle Rosa Mygale Grauvogeli": {
        "description": "Permet à son utilisateur de devenir entièrement ou partiellement une Rosa mygale Grauvogeli.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Zo Zo no mi modèle Mammouth": {
        "description": "Permet à son utilisateur de devenir entièrement ou partiellement un mammouth.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Ryu Ryu no mi modèle Allosaure": {
        "description": "Permet à son utilisateur de devenir entièrement ou partiellement un Allosaure.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Ryu Ryu no mi modèle Spinosaure": {
        "description": "Permet à son utilisateur de devenir entièrement ou partiellement un Spinosaure.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Ryu Ryu no mi modèle Ptéranodon": {
        "description": "Permet à son utilisateur de devenir entièrement ou partiellement un Ptéranodon.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Ryu Ryu no mi modèle Prachéchyosaure": {
        "description": "Permet à son utilisateur de devenir entièrement ou partiellement un Pachycéphalosaure.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Ryu Ryu no mi modèle Tricératops": {
        "description": "Permet à son utilisateur de devenir entièrement ou partiellement un Tricératops.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Ryu Ryu no mi modèle Brachiosaure": {
        "description": "Permet à son utilisateur de devenir entièrement ou partiellement un Brachiosaure.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    }
}

logia = {
     "Moku Moku no mi": {
        "description": "Permet à l'utilisateur de créer, contrôler et se transformer en fumée.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Mera Mera no mi": {
        "description": "Permet à l'utilisateur de créer, contrôler et se transformer en flammes.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Magu Magu no mi": {
        "description": "Permet à l'utilisateur de créer, contrôler et se transformer en magma.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Suna Suna no mi": {
        "description": "Permet à l'utilisateur de créer, contrôler et se transformer en sable.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Goro Goro no mi": {
        "description": "Permet à l'utilisateur de créer, contrôler et se transformer en électricité.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Hie Hie no mi": {
        "description": "Permet à l'utilisateur de créer, contrôler et se transformer en glace.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Yuki Yuki no mi": {
        "description": "Permet à l'utilisateur de créer, contrôler et se transformer en neige.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Mori Mori no mi": {
        "description": "Permet à l'utilisateur de créer, contrôler et se transformer en végétaux.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Susu Susu no mi": {
        "description": "Permet à l'utilisateur de créer, contrôler et se transformer en suie.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Numa Numa no mi": {
        "description": "Permet à l'utilisateur de créer, contrôler et se transformer en marais.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Toro Toro no mi": {
        "description": "Permet à l'utilisateur de créer, contrôler et se transformer en liquide.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Pasa Pasa no mi": {
        "description": "Permet à l'utilisateur de créer, contrôler et se transformer en papier ainsi que contrôler ce qui est inscrit dessus.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Ame Ame no mi": {
        "description": "Permet à l'utilisateur de créer, contrôler et se transformer en sirop visqueux.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Pika Pika no mi": {
        "description": "Permet à l'utilisateur de créer, contrôler et se transformer en lumière.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    }
}

zoan_mythique = {
   "Hito Hito no mi modèle Onyudu": {
        "description": "Permet à son utilisateur de devenir entièrement ou partiellement un moine onyudu.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Hito Hito no mi modèle Daibutsu": {
        "description": "Permet à son utilisateur de devenir entièrement ou partiellement un géant Daibutsu, statue d’or de bouddha.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Hebi Hebi no mi modèle Yamata no Orochi": {
        "description": "Permet à son utilisateur de devenir entièrement ou partiellement une hydre à 8 têtes.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Uo Uo no mi modèle Seiryu": {
        "description": "Permet à son utilisateur de devenir entièrement ou partiellement un dragon azur.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Inu Inu no mi modèle Okuchi no Makami": {
        "description": "Permet à son utilisateur de devenir entièrement ou partiellement un loup divin.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Inu Inu no mi modèle Kyubi no Kitsune": {
        "description": "Permet à son utilisateur de devenir entièrement ou partiellement un Kyubi, renard à 9 queues.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Uma Uma no mi modèle Pégase": {
        "description": "Permet à son utilisateur de devenir entièrement ou partiellement un pégase.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Tori Tori no mi modèle Phénix": {
        "description": "Permet à son utilisateur de devenir entièrement ou partiellement un phénix ardent.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Tori Tori no mi modèle Nue": {
        "description": "Permet à son utilisateur de devenir entièrement ou partiellement une nue mythologique, espèce de créature volante et enflammée à tête de singe, corps de lion et griffes de tigre.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Bato Bato no mi modèle Vampire": {
        "description": "Permet à son utilisateur de devenir entièrement ou partiellement un vampire, homme chauve-souris mythologique.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    }
}

paramecias_corporel = {
    "Gomu Gomu no mi": {
        "description": "Permet à l'utilisateur de devenir aussi élastique que du caoutchouc.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Bara Bara no mi": {
        "description": "Permet à l'utilisateur de fragmenter son corps, le rendant insensible à toute lame.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Beri Beri no mi": {
        "description": "Permet à l'utilisateur de fragmenter son corps en boules de différentes tailles, le rendant insensible aux attaques à mains nues.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Sube Sube no mi": {
        "description": "Permet à l'utilisateur d’avoir le corps plus glissant que du beurre fondu.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Kilo Kilo no mi": {
        "description": "Permet à l'utilisateur de changer son poids de 1kg jusqu'à 10 000 kg.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Ton Ton no mi": {
        "description": "Permet à l'utilisateur de faire varier son poids (semble avoir moins de limite que le kilo).",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Bomu Bomu no mi": {
        "description": "Permet à l'utilisateur de créer une explosion à partir de n’importe quelle partie de son corps.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Baku Baku no mi": {
        "description": "Permet à l'utilisateur de manger toute matière sans problème digestif pour en acquérir les propriétés.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Mane Mane no mi": {
        "description": "Permet à l'utilisateur de copier le visage de n’importe qui après l’avoir touché.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Supa Supa no mi": {
        "description": "Permet à l'utilisateur de transformer n’importe quelle partie de son corps en sabre tranchant.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Toge Toge no mi": {
        "description": "Permet à l'utilisateur de créer comme des piques d’oursin sur n’importe quelle partie de son corps.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Bane Bane no mi": {
        "description": "Permet à l'utilisateur de transformer n’importe quelle partie de son corps en ressort.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Shari Shari no mi": {
        "description": "Permet à l'utilisateur de faire tourner n’importe quelle partie de son corps comme une roue.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Suke Suke no mi": {
        "description": "Permet à l'utilisateur de devenir invisible.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Shiro Shiro no mi": {
        "description": "Permet à l'utilisateur de devenir une forteresse vivante pouvant transporter des personnes et objets miniaturisés.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Fruit d’Urouge": {
        "description": "Permet à l'utilisateur de convertir les dégâts reçus en taille et en puissance brute.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Choki Choki no mi": {
        "description": "Permet à l'utilisateur de transformer son corps en ciseaux d’un tranchant extrême.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Kira Kira no mi": {
        "description": "Permet à l'utilisateur de transformer son corps en diamant, le rendant d’une immense résistance.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Poke Poke no mi": {
        "description": "Permet à l'utilisateur d’avoir des poches sur son corps pour ranger sans limite des objets de grande taille.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Deka Deka no mi": {
        "description": "Permet à l'utilisateur d'augmenter sa taille considérablement.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Buki Buki no mi": {
        "description": "Permet à l'utilisateur de transformer son corps en toutes sortes d’armes.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Guru Guru no mi": {
        "description": "Permet à l'utilisateur de changer des parties de son corps en hélices pour s’envoler.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Jake Jake no mi": {
        "description": "Permet à l'utilisateur de devenir une veste pouvant être enfilé par un autre individu.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Pamu Pamu no mi": {
        "description": "Permet à l'utilisateur de faire éclater des parties de son corps pour produire des explosions.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Kibi Kibi no mi": {
        "description": "Permet à l'utilisateur de créer à partir de son corps des mochi pouvant aider à apprivoiser des créatures sauvages.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Netsu Netsu no mi": {
        "description": "Permet à l'utilisateur de chauffer à une température extrême son corps peuvent même s'enflammer.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Riki Riki no mi": {
        "description": "Permet à l'utilisateur d'augmenter à un niveau extrême sa force.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Nomi Nomi no mi": {
        "description": "Permet à l'utilisateur d’avoir une mémoire sans limite.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Kama Kama no mi": {
        "description": "Permet à l'utilisateur de créer des lames d’airs à partir de ces ongles devenus longs et tranchants.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Kachi Kachi no mi": {
        "description": "Permet à l'utilisateur d’augmenter la température et la résistance de son corps.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Atsu Atsu no mi": {
        "description": "Permet à l'utilisateur de faire émaner de son corps de la chaleur jusqu'à 10 000 degrés.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Bana Bana no mi": {
        "description": "Permet à l'utilisateur de convertir son sentiment de jalousie en chaleur, au point de pouvoir s'enflammer.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Gutsu Gutsu no mi": {
        "description": "Permet à l'utilisateur de pouvoir faire fondre le métal pour le forger sans outil ni support.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Mini Mini no mi": {
        "description": "Permet à l'utilisateur de rétrécir jusqu’à 5 millimètres.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Ami Ami no mi": {
        "description": "Permet à l'utilisateur de créer et devenir des filets.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Nito Nito no mi": {
        "description": "Permet à l'utilisateur de produire de la nitroglycérine par sa transpiration, pouvant faire exploser ce dernier.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Koro Koro no mi": {
        "description": "Permet à l'utilisateur de devenir entièrement ou partiellement un wagon.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Nibi Nibi no mi": {
        "description": "Permet à l'utilisateur de reproduire l'apparence d’une personne décédée (ne copie pas les capacités).",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Gero Gero no mi": {
        "description": "Permet à l'utilisateur de produire en permanence une odeur répugnante.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    }
}

paramecias_productif = {
    "Hana Hana no mi": {
        "description": "Permet à l'utilisateur de générer des membres de son corps sur n’importe quelle surface autour.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Doru Doru no mi": {
        "description": "Permet à l'utilisateur de générer et manipuler de la cire.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Ori Ori no mi": {
        "description": "Permet à l'utilisateur de créer des anneaux et des barreaux d’acier.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Ito Ito no mi": {
        "description": "Permet à l'utilisateur de créer et contrôler des fils fins.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Awa Awa no mi": {
        "description": "Permet à l'utilisateur de créer et manipuler des bulles de savon.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Doku Doku no mi": {
        "description": "Permet à l'utilisateur de créer et manipuler toutes sortes de poisons en plus d’y être insensible.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Fuku Fuku no mi": {
        "description": "Permet à l'utilisateur de créer des vêtements en tout genre.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Beta Beta no mi": {
        "description": "Permet à l'utilisateur de générer et manipuler du mucus.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Pero Pero no mi": {
        "description": "Permet à l'utilisateur de générer et manipuler des bonbons et de la gélatine.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Bisu Bisu no mi": {
        "description": "Permet à l'utilisateur de créer et manipuler des biscuits en frappant des mains.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Kuri Kuri no mi": {
        "description": "Permet à l'utilisateur de créer et manipuler de la crème brûlée.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Bata Bata no mi": {
        "description": "Permet à l'utilisateur de créer et contrôler du beurre doux.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Bari Bari no mi": {
        "description": "Permet à l'utilisateur de créer des barrières incassables en croisant des doigts.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Goe Goe no mi": {
        "description": "Permet à l'utilisateur de produire des faisceaux sonores similaires à des rayons d’énergie.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Noko Noko no mi": {
        "description": "Permet à l'utilisateur de produire des spores toxiques de champignons.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Jara Jara no mi": {
        "description": "Permet à l'utilisateur de produire des chaînes d’acier à partir de son corps.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Nepa Nepa no mi": {
        "description": "Permet à l'utilisateur de produire des vagues de chaleur et de flammes.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Mono Mono no mi": {
        "description": "Permet à l'utilisateur de créer des clones de lui-même, de quelqu’un d’autre ou d’un objet.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Bai Bai no mi": {
        "description": "Permet à l'utilisateur de créer des répliques de n’importe quel objet non organique.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Mochi Mochi no mi": {
        "description": "Permet à l'utilisateur de créer, contrôler et se transformer en riz gluant.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Meta Meta no mi": {
        "description": "Permet à l'utilisateur de créer, contrôler et se transformer en métal liquide.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    }
}

paramecias_manipulateur = {
    "Noro Noro no Mi": {
        "description": "Permet à l'utilisateur de tirer un rayon qui ralenti les cibles de 30 fois pendant 30 secondes.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Doa Doa no Mi": {
        "description": "Permet à l'utilisateur de créer des portes n’importe où pour se déplacer vers une autre dimension.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Sabi Sabi no Mi": {
        "description": "Permet à l'utilisateur de faire rouiller tout le fer qu’il touche.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Yomi Yomi no Mi": {
        "description": "Permet à l'utilisateur de devenir immortel et de contrôler son esprit hors de son corps.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Kage Kage no Mi": {
        "description": "Permet à l'utilisateur de prendre, manipuler les ombres ainsi que d’en changer les propriétaires.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Horo Horo no Mi": {
        "description": "Permet à l'utilisateur de générer des fantômes déprimants en plus de pouvoir acquérir une forme spectrale hors de son corps.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Jiki Jiki no Mi": {
        "description": "Permet à l'utilisateur de contrôler l'électromagnétisme pour ainsi manipuler le fer autour.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Gura Gura no Mi": {
        "description": "Permet à l'utilisateur de créer des ondes sismiques dévastatrices sur terre comme au ciel, et même en mer.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Woshu Woshu no Mi": {
        "description": "Permet à l'utilisateur d’agir sur les personnes et objets l’entourant comme du linge à laver et étendre.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Fuwa Fuwa no Mi": {
        "description": "Permet à l'utilisateur de faire voler tout objet non vivant à condition de l’avoir touché au préalable.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Mato Mato no Mi": {
        "description": "Permet à l'utilisateur de ne jamais rater sa cible lorsqu’il lance un objet.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Zushi Zushi no Mi": {
        "description": "Permet à l'utilisateur de manipuler la gravité.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Nui Nui no Mi": {
        "description": "Permet à l'utilisateur de coudre ses adversaires et son environnement.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Giro Giro no Mi": {
        "description": "Permet à l'utilisateur de voir à travers toute matière ainsi que de sonder l’esprit des gens.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Ato Ato no Mi": {
        "description": "Permet à l'utilisateur de transformer ce qui l'entoure en œuvre d’art grâce à des nuages artistiques.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Sui Sui no Mi": {
        "description": "Permet à l'utilisateur de nager sur toute surface hors de l’eau.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Hira Hira no Mi": {
        "description": "Permet à l'utilisateur de rendre toute chose rigide aussi flexible qu’un drapeau.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Ishi Ishi no Mi": {
        "description": "Permet à l'utilisateur de manipuler la roche de son environnement.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Fude Fude no Mi": {
        "description": "Permet à l'utilisateur de donner vie à ses dessins.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Nagi Nagi no Mi": {
        "description": "Permet à l'utilisateur d’annuler tous bruits qu’il produit ou qui sont produits dans une zone établie, ou bien d'isoler le son intérieur de sa zone avec celui extérieur.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Chiyu Chiyu no Mi": {
        "description": "Permet à l'utilisateur de soigner rapidement toutes blessures.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Maki Maki no Mi": {
        "description": "Permet à l'utilisateur de créer et contrôler des parchemins de différentes tailles pour y stocker des objets.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Soru Soru no Mi": {
        "description": "Permet à l'utilisateur de prendre l'espérance de vie d’un individu pour augmenter la sienne, ou bien donner vie à des objets non organiques.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Mira Mira no Mi": {
        "description": "Permet à l'utilisateur de créer et contrôler des miroirs ainsi que de les lier à une dimension parallèle.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Buku Buku no Mi": {
        "description": "Permet à l'utilisateur de créer et contrôler des livres pouvant être liés à une dimension parallèle.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Shibo Shibo no Mi": {
        "description": "Permet à l'utilisateur d’essorer n’importe quelle forme de vie afin d’en extraire les liquides vitaux. Il peut également augmenter en taille grâce à ce liquide.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Memo Memo no Mi": {
        "description": "Permet à l'utilisateur d’extraire la mémoire d’un individu sous forme de pellicule cinématographique pour la manipuler.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Hoya Hoya no Mi": {
        "description": "Permet à l'utilisateur de créer et contrôler un génie se battant à ses côtés. Stand power.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Kuku Kuku no Mi": {
        "description": "Permet à l'utilisateur de cuisiner toute matière de son environnement. Mais cela a un goût ignoble.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Gocha Gocha no Mi": {
        "description": "Permet à l'utilisateur de fusionner avec d’autres personnes.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Kobu Kobu no Mi": {
        "description": "Permet à l'utilisateur d’éveiller le potentiel de combat latent des individus autour tout en les reliant au combat.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Oshi Oshi no Mi": {
        "description": "Permet à l'utilisateur de manipuler le sol pour le faire vibrer comme des vagues ou créer des tunnels souterrains.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Juku Juku no Mi": {
        "description": "Permet à l'utilisateur de faire mûrir toute chose, que ce soit augmenter l’âge physique d’un individu ou vieillir son environnement jusqu'à sa putréfaction.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Shiku Shiku no Mi": {
        "description": "Permet à l'utilisateur de contaminer un individu avec toutes sortes de maladies qu’il peut créer, y compris des maladies inconnues comme celle qui change le sexe d’un individu.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Wapu Wapu no Mi": {
        "description": "Permet à l'utilisateur de se téléporter.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Shima Shima no Mi": {
        "description": "Permet à l'utilisateur de fusionner avec une île pour la contrôler.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Gabu Gabu no Mi": {
        "description": "Permet à l'utilisateur de contrôler l’alcool.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Muchi Muchi no Mi": {
        "description": "Permet à l'utilisateur de transformer des objets en fouet ainsi que de soumettre d’autres objets qu’il contrôle comme des esclaves.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Nori Nori no Mi": {
        "description": "Permet à l'utilisateur de chevaucher toutes choses.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Hiso Hiso no Mi": {
        "description": "Permet à l'utilisateur de comprendre les animaux ainsi que de pouvoir parler avec eux.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Mosa Mosa no Mi": {
        "description": "Permet à l'utilisateur de faire pousser rapidement des plantes pour manipuler celles-ci.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Moa Moa no Mi": {
        "description": "Permet à l'utilisateur de renforcer jusqu'à 100 fois la force, la taille et la vitesse de ce qu’il touche.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Kyubu Kyubu no Mi": {
        "description": "Permet à l'utilisateur de fragmenter et transformer ce qu’il touche en cube.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Hore Hore no Mi": {
        "description": "Permet à l'utilisateur de devenir extrêmement charmant, pouvant faire tomber les gens amoureux de lui.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Nuke Nuke no Mi": {
        "description": "Permet à l'utilisateur de passer à travers toute matière non organique.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Iro Iro no Mi": {
        "description": "Permet à l'utilisateur de se peindre rapidement lui-même, quelqu’un d’autre et/ou un objet afin de se camoufler dans son environnement.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Gol Gol no Mi": {
        "description": "Permet à l'utilisateur de contrôler l’or de son environnement.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Ute Ute no Mi": {
        "description": "Permet à l'utilisateur de transformer toute chose non organique qu’il touche en pistolet et canon.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Pocha Pocha no Mi": {
        "description": "Permet à l'utilisateur de faire grossir le corps de quelqu’un.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Deri Deri no Mi": {
        "description": "Permet à l'utilisateur de livrer des objets à n'importe qui dans son champ de vision.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Gemu Gemu no Mi": {
        "description": "Permet à l'utilisateur de créer une dimension qu’il domine semblable à un jeu vidéo qu’il peut modifier.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Chara Chara no Mi": {
        "description": "Permet à l'utilisateur de donner une conscience aux âmes non vivantes ainsi que de fusionner avec d’autres personnes et/ou objets rendus conscients.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Basu Basu no Mi": {
        "description": "Permet à l'utilisateur de transformer tout ce qu’il touche en bombe.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Gasha Gasha no Mi": {
        "description": "Permet à l'utilisateur de manipuler et assembler la matière non organique de son environnement.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Kote Kote no Mi": {
        "description": "Permet à l'utilisateur d'invoquer des gantelets géants qu’il peut manipuler à sa guise pour saisir toute chose non vivante.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    }

}


fdd_list = {
    **paramecias_corporel,
    **paramecias_productif,
    **paramecias_manipulateur,
    **logia,
    **zoan_classique,
    **zoan_antique,
    **zoan_mythique
}

STAFF_ROLES_IDS = [1269838005234044958, 1269837965446610985]  # Modo et Admin


@bot.group(name="fdd", invoke_without_command=True)
async def fdd(ctx):
    """Groupe de commandes pour les fruits du démon."""
    await ctx.send("Utilisez `?fdd liste`, `?fdd inventaire`, ou `?fdd add/remove` pour accéder aux commandes des fruits du démon.")

@fdd.command(name="inventaire")
async def fdd_inventaire(ctx, member: discord.Member = None):
    """Affiche l'inventaire des fruits du démon d'un utilisateur avec l'état 'mangé' si applicable."""
    member = member or ctx.author

    async with aiosqlite.connect('inventory.db') as db:
        # Requête pour récupérer les fruits possédés par l'utilisateur et leur état (mangé ou non)
        query = """
            SELECT fdd_name, eaten
            FROM fdd_inventory
            WHERE user_id = ?
        """
        cursor = await db.execute(query, (member.id,))
        rows = await cursor.fetchall()

    # Log pour vérifier les fruits récupérés
    logging.info(f"Fetched rows for user {member.id}: {rows}")

    if not rows:
        await ctx.send(f"{member.mention} ne possède aucun fruit du démon.")
        return

    # Créer un dictionnaire pour trier les fruits par sous-catégorie
    sorted_fruits = {
        "Paramecia Corporel": [],
        "Paramecia Productif": [],
        "Paramecia Manipulateur": [],
        "Logia": [],
        "Zoan Classique": [],
        "Zoan Antique": [],
        "Zoan Mythique": [],
    }

    # Trier les fruits par sous-catégorie et ajouter "(mangé)" si le fruit est mangé
    for fruit_name, eaten in rows:
        fruit_status = " (mangé)" if eaten == "True" else ""
        # Vérifier si le fruit existe dans fdd_list
        if fruit_name in fdd_list:
            fruit = fdd_list[fruit_name]
            # Récupérer la catégorie du fruit
            if fruit_name in paramecias_corporel:
                sorted_fruits["Paramecia Corporel"].append(f"{fruit_name}{fruit_status}")
            elif fruit_name in paramecias_productif:
                sorted_fruits["Paramecia Productif"].append(f"{fruit_name}{fruit_status}")
            elif fruit_name in paramecias_manipulateur:
                sorted_fruits["Paramecia Manipulateur"].append(f"{fruit_name}{fruit_status}")
            elif fruit_name in logia:
                sorted_fruits["Logia"].append(f"{fruit_name}{fruit_status}")
            elif fruit_name in zoan_classique:
                sorted_fruits["Zoan Classique"].append(f"{fruit_name}{fruit_status}")
            elif fruit_name in zoan_antique:
                sorted_fruits["Zoan Antique"].append(f"{fruit_name}{fruit_status}")
            elif fruit_name in zoan_mythique:
                sorted_fruits["Zoan Mythique"].append(f"{fruit_name}{fruit_status}")
        else:
            # Si le fruit n'est pas trouvé, on l'ajoute dans une catégorie inconnue
            if "Inconnue" not in sorted_fruits:
                sorted_fruits["Inconnue"] = []
            sorted_fruits["Inconnue"].append(f"{fruit_name}{fruit_status}")

    logging.info(f"Sorted fruits for user {member.id}: {sorted_fruits}")

    # Création de l'embed d'inventaire
    embed = discord.Embed(
        title=f"Inventaire des Fruits du Démon de {member.display_name}",
        color=0xFFBF66
    )

    has_content = False
    for category, fruits in sorted_fruits.items():
        if fruits:
            has_content = True
            value = "\n".join(f"**{fruit_name}**" for fruit_name in fruits)
            embed.add_field(name=category, value=value, inline=False)

    if not has_content:
        embed.description = "Aucun fruit dans l'inventaire."

    logging.info(f"Embed content: {embed.to_dict()}")
    await ctx.send(embed=embed)

@fdd.command(name="liste")
async def fdd_liste(ctx):
    """Affiche un menu pour choisir une catégorie de fruits du démon."""
    # Options pour le menu déroulant
    options = [
        discord.SelectOption(label="Paramecia Corporel", description="Voir les Paramecia Corporel", emoji="\ud83c\udfcb️"),
        discord.SelectOption(label="Paramecia Productif", description="Voir les Paramecia Productif", emoji="⚙️"),
        discord.SelectOption(label="Paramecia Manipulateur", description="Voir les Paramecia Manipulateur", emoji="🎭"),
        discord.SelectOption(label="Logia", description="Voir les Logia", emoji="🔥"),
        discord.SelectOption(label="Zoan Classique", description="Voir les Zoan Classiques", emoji="🐯"),
        discord.SelectOption(label="Zoan Antique", description="Voir les Zoan Antiques", emoji="🧖"),
        discord.SelectOption(label="Zoan Mythique", description="Voir les Zoan Mythiques", emoji="🐉"),
    ]

    # Création du menu déroulant
    select = Select(placeholder="Choisissez une catégorie de FDD", options=options)

    # Callback du menu déroulant
    async def callback(interaction: discord.Interaction):
        category = interaction.data["values"][0]  # Récupère la catégorie sélectionnée

        async with aiosqlite.connect('inventory.db') as db:
            # Construction de la liste des fruits correspondant à la catégorie
            all_fruits = {
                "Paramecia Corporel": list(paramecias_corporel),
                "Paramecia Productif": list(paramecias_productif),
                "Paramecia Manipulateur": list(paramecias_manipulateur),
                "Logia": list(logia),
                "Zoan Classique": list(zoan_classique),
                "Zoan Antique": list(zoan_antique),
                "Zoan Mythique": list(zoan_mythique),
            }.get(category, [])

            # Construction dynamique de placeholders pour la requête SQL
            placeholders = ', '.join(['?'] * len(all_fruits))
            query = f"SELECT fdd_name, eaten FROM fdd_inventory WHERE fdd_name IN ({placeholders}) AND user_id IS NOT NULL"
            cursor = await db.execute(query, all_fruits)
            rows = await cursor.fetchall()

            # Fruits déjà pris avec indication "mangé" si nécessaire
            fruits_pris = [(f"{row[0]} (mangé)" if row[1] == "True" else row[0]) for row in rows]

            # Fruits disponibles
            fruits_disponibles = [fruit for fruit in all_fruits if fruit not in [row[0] for row in rows]]

            # Préparer les sections pour l'embed
            pris_section = "\n".join(fruits_pris) if fruits_pris else "Aucun fruit pris."
            dispo_section = "\n".join(fruits_disponibles) if fruits_disponibles else "Aucun fruit disponible."

            # Création de l'embed
            embed = discord.Embed(
                title=f"Fruits du Démon - {category}",
                color=0xFFBF66
            )
            embed.add_field(name="Fruits Pris", value=pris_section, inline=False)
            embed.add_field(name="Fruits Disponibles", value=dispo_section, inline=False)

            # Envoi de l'embed
            await interaction.response.send_message(embed=embed)

    # Ajouter le callback au menu
    select.callback = callback

    # Ajouter le menu dans une vue
    view = View()
    view.add_item(select)

    # Envoyer le menu
    await ctx.send("Choisissez une catégorie de Fruits du Démon :", view=view)

@fdd.command(name="add")
async def fdd_add(ctx, fruit_name: str, member: discord.Member):
    """Ajoute un fruit du démon à l'inventaire d'un utilisateur (réservée au staff)."""
    # Vérifier si l'utilisateur a un des rôles de staff (Modo ou Admin)
    if not any(role.id in STAFF_ROLES_IDS for role in ctx.author.roles):
        await ctx.send(f"{ctx.author.mention}, vous n'avez pas la permission d'exécuter cette commande.")
        return

    if fruit_name not in fdd_list:
        await ctx.send(f"Le fruit {fruit_name} n'existe pas dans la base de données.")
        return

    async with aiosqlite.connect('inventory.db') as db:
        # Vérifier si le fruit est déjà possédé
        query_check = """
            SELECT user_id FROM fdd_inventory WHERE fdd_name = ?
        """
        cursor = await db.execute(query_check, (fruit_name,))
        row = await cursor.fetchone()

        if row and row[0]:
            await ctx.send(f"Le fruit {fruit_name} est déjà possédé par quelqu'un.")
            return

        # Ajouter le fruit à l'utilisateur
        query_insert = """
            INSERT OR REPLACE INTO fdd_inventory (fdd_name, user_id) VALUES (?, ?)
        """
        await db.execute(query_insert, (fruit_name, member.id))
        await db.commit()

    await ctx.send(f"{member.mention} a reçu le fruit {fruit_name} !")

@fdd.command(name="remove")
async def fdd_remove(ctx, fruit_name: str, member: discord.Member):
    """Retire un fruit du démon de l'inventaire d'un utilisateur (réservée au staff)."""
    # Vérifier si l'utilisateur a un des rôles de staff (Modo ou Admin)
    if not any(role.id in STAFF_ROLES_IDS for role in ctx.author.roles):
        await ctx.send(f"{ctx.author.mention}, vous n'avez pas la permission d'exécuter cette commande.")
        return

    async with aiosqlite.connect('inventory.db') as db:
        # Vérifier si l'utilisateur possède le fruit
        query_check = """
            SELECT user_id FROM fdd_inventory WHERE fdd_name = ? AND user_id = ?
        """
        cursor = await db.execute(query_check, (fruit_name, member.id))
        row = await cursor.fetchone()

        if not row:
            await ctx.send(f"{member.mention} ne possède pas le fruit {fruit_name}.")
            return

        # Retirer le fruit de l'utilisateur
        query_delete = """
            DELETE FROM fdd_inventory WHERE fdd_name = ? AND user_id = ?
        """
        await db.execute(query_delete, (fruit_name, member.id))
        await db.commit()

    await ctx.send(f"Le fruit {fruit_name} a été retiré de l'inventaire de {member.mention}.")

@fdd.command(name="info")
async def fdd_info(ctx, *, fruit_name: str):
    """Affiche les informations détaillées d'un fruit du démon avec son propriétaire.""" 
    # Vérifier si le fruit existe dans la base de données
    if fruit_name not in fdd_list:
        await ctx.send(f"Le fruit du démon {fruit_name} n'existe pas.")
        return

    # Accéder à la base de données pour récupérer les informations sur le fruit
    async with aiosqlite.connect('inventory.db') as db:
        # Récupérer l'ID de l'utilisateur et le statut "mangé"
        query = """
            SELECT user_id, eaten FROM fdd_inventory WHERE fdd_name = ?
        """
        cursor = await db.execute(query, (fruit_name,))
        row = await cursor.fetchone()

    # Si le fruit n'a pas été trouvé dans l'inventaire
    if row is None:
        await ctx.send(f"Le fruit {fruit_name} n'est pas encore possédé.")
        return

    # Récupérer l'utilisateur possédant le fruit
    owner_id = row[0]
    eaten_status = "Oui" if row[1] == "True" else "Non"

    # Obtenir l'objet utilisateur à partir de l'ID
    owner = await ctx.bot.fetch_user(owner_id)

    # Récupérer la description du fruit depuis `fdd_list`
    fruit_info = fdd_list.get(fruit_name)
    description = fruit_info["description"]

    # Créer l'embed
    embed = discord.Embed(
        title=f"Informations sur le fruit du démon : {fruit_name}",
        description=description,
        color=0xFFBF66
    )

    # Ajouter le statut "Mangé" et le propriétaire à l'embed
    embed.add_field(name="Mangé ?", value=eaten_status, inline=False)
    embed.add_field(name="Propriétaire", value=owner.mention, inline=False)

    # Ajouter l'image du fruit (vignette) si disponible
    embed.set_thumbnail(url=fruit_info["embed"].thumbnail.url)

    # Envoyer l'embed
    await ctx.send(embed=embed)

@fdd.command(name="manger")
async def fdd_manger(ctx, fruit_name: str):
    """Permet à un utilisateur de manger un fruit du démon, s'il n'en a pas déjà mangé un."""
    async with aiosqlite.connect('inventory.db') as db:
        # Vérifier si l'utilisateur a déjà mangé un fruit
        query_check = """
            SELECT fdd_name FROM fdd_inventory
            WHERE user_id = ? AND eaten = 'True'
        """
        cursor = await db.execute(query_check, (ctx.author.id,))
        row = await cursor.fetchone()

        if row:
            # Si l'utilisateur a déjà mangé un fruit, on lui dit qu'il ne peut pas en manger un autre
            await ctx.send(f"{ctx.author.mention}, vous avez déjà mangé un fruit du démon. Vous ne pouvez pas en manger un autre.")
            return

        # Vérifier si le fruit demandé existe et s'il appartient à l'utilisateur
        query_check_fruit = """
            SELECT eaten FROM fdd_inventory WHERE user_id = ? AND fdd_name = ?
        """
        cursor = await db.execute(query_check_fruit, (ctx.author.id, fruit_name))
        row = await cursor.fetchone()

        if not row:
            # Si l'utilisateur ne possède pas ce fruit
            await ctx.send(f"{ctx.author.mention}, vous ne possédez pas le fruit {fruit_name}.")
            return

        if row[0] == "True":
            # Si le fruit est déjà mangé, on l'informe
            await ctx.send(f"{ctx.author.mention}, vous avez déjà mangé le fruit {fruit_name}.")
            return

        # Marquer le fruit comme mangé
        query_update = """
            UPDATE fdd_inventory
            SET eaten = 'True'
            WHERE user_id = ? AND fdd_name = ?
        """
        await db.execute(query_update, (ctx.author.id, fruit_name))
        await db.commit()

        # Message de confirmation
        await ctx.send(f"{ctx.author.mention} a mangé le fruit {fruit_name} ! Vous ne pouvez plus manger d'autres fruits.")

@fdd.command(name="trade")
async def fdd_trade(ctx, fruit_name: str, member: discord.Member):
    """Permet de transférer un fruit du démon à un autre utilisateur si les deux parties acceptent."""
    async with aiosqlite.connect('inventory.db') as db:
        # Vérifier si le fruit appartient à l'utilisateur qui propose l'échange
        query_check = """
            SELECT user_id, eaten FROM fdd_inventory
            WHERE fdd_name = ? AND user_id = ?
        """
        cursor = await db.execute(query_check, (fruit_name, ctx.author.id))
        row = await cursor.fetchone()

        if not row:
            # Si le fruit n'appartient pas à l'utilisateur
            await ctx.send(f"{ctx.author.mention}, vous ne possédez pas le fruit {fruit_name}.")
            return

        if row[1] == "True":
            # Si le fruit a été mangé
            await ctx.send(f"{ctx.author.mention}, vous ne pouvez pas échanger le fruit {fruit_name} car il a déjà été mangé.")
            return

    # Demander confirmation à l'autre utilisateur
    await ctx.send(f"{member.mention}, {ctx.author.mention} souhaite vous donner le fruit **{fruit_name}**. Répondez `oui` pour accepter l'échange.")

    def check(message):
        return (
            message.author == member
            and message.channel == ctx.channel
            and message.content.lower() in ["oui", "non"]
        )

    try:
        # Attendre la réponse de l'utilisateur mentionné
        response = await bot.wait_for("message", check=check, timeout=60.0)
    except asyncio.TimeoutError:
        await ctx.send(f"{member.mention} n'a pas répondu à temps. L'échange est annulé.")
        return

    if response.content.lower() == "non":
        await ctx.send(f"{member.mention} a refusé l'échange.")
        return

    # Effectuer le transfert
    async with aiosqlite.connect('inventory.db') as db:
        query_update = """
            UPDATE fdd_inventory
            SET user_id = ?
            WHERE fdd_name = ? AND user_id = ?
        """
        await db.execute(query_update, (member.id, fruit_name, ctx.author.id))
        await db.commit()

    # Confirmation de l'échange
    await ctx.send(f"L'échange a été effectué avec succès ! {member.mention} possède maintenant le fruit **{fruit_name}**.")

# Dictionnaire de mappage des techniques avec les noms de colonnes de la base de données
technique_column_mapping = {
    "Ittôryû": "ittoryu",
    "Nitôryû": "nitoryu",
    "Santôryû": "santoryu",
    "Mûtôryû": "mutoryu",
    "Style du Renard de Feu": "style_du_renard_de_feu",
    "Danse de l'Épée des Remous": "danse_de_lepee_des_remous",
    "Style de Combat Tireur d'Élite": "style_de_combat_tireur_delite",
    "Balle Explosive": "balle_explosive",
    "Balle Incendiaire": "balle_incendiaire",
    "Balle Fumigène": "balle_fumigene",
    "Balle Dégoutante": "balle_degoutante",
    "Balle Cactus": "balle_cactus",
    "Balle Venimeuse": "balle_venimeuse",
    "Balle Électrique": "balle_electrique",
    "Balle Gelante": "balle_gelante",
    "Green Pop": "green_pop",
    "Karaté": "karate",
    "Taekwondo": "taekwondo",
    "Judo": "judo",
    "Boxe": "boxe",
    "Okama Kenpo": "okama_kenpo",
    "Hassoken": "hassoken",
    "Ryusoken": "ryusoken",
    "Jambe noire": "jambe_noire",
    "Gyojin Karaté (simplifié)": "gyojin_karate_simplifie",
    "Rope Action": "rope_action",
    "Ramen Kenpo": "ramen_kenpo",
    "Gyojin Karaté": "gyojin_karate",
    "Art Martial Tontatta": "art_martial_tontatta",
    "Jao Kun Do": "jao_kun_do",
    "Electro": "electro",
    "Sulong": "sulong",
    "Style Personnel": "style_personnel"
}


# Fonction pour créer un menu déroulant pour les catégories
class SkillCategorySelect(Select):
    def __init__(self, categories):
        options = [discord.SelectOption(label=category) for category in categories]
        super().__init__(placeholder="Choisissez une catégorie", options=options)

    async def callback(self, interaction: discord.Interaction):
        category = self.values[0]
        user_id = interaction.user.id 

        # Vérification si l'utilisateur existe dans la base de données
        async with aiosqlite.connect('inventory.db') as db:
            cursor = await db.execute("SELECT * FROM skills WHERE user_id = ?", (user_id,))
            user_data = await cursor.fetchone()

            if user_data is None:
                # Initialisation de l'utilisateur dans la base de données si nécessaire
                await db.execute("INSERT INTO skills (user_id) VALUES (?)", (user_id,))
                await db.commit()
                await interaction.response.send_message(f"L'utilisateur {interaction.user.name} a été initialisé dans la base de données.", ephemeral=True)

        # Créer l'embed avec les techniques de la catégorie sélectionnée
        embed = discord.Embed(title=f"Techniques de {category}", color=0xFFBF66)
        
        for technique, _ in skills_liste[category].items():
            # Trouver le nom de la colonne correspondant à la technique
            technique_column = technique_column_mapping.get(technique, technique.lower().replace(" ", "_").replace("é", "e"))
            
            async with aiosqlite.connect('inventory.db') as db:
                cursor = await db.execute(f"SELECT {technique_column} FROM skills WHERE user_id = ?", (user_id,))
                palier = await cursor.fetchone()
                
                palier_str = "``Techniques non apprise``"
                if palier and palier[0] > 0:
                    palier_str = ["I", "II", "III", "IV", "V", "X"][palier[0] - 1] if palier[0] <= 6 else "X"
                
                embed.add_field(name=technique, value=f"Palier: {palier_str}", inline=False)

        await interaction.response.send_message(embed=embed)

# Fonction pour afficher les informations de base
@bot.group(invoke_without_command=True)
async def skills(ctx):
    """
    Commande de groupe 'skills' qui sert de parent à toutes les commandes liées aux compétences.
    """
    categories = list(skills_liste.keys())  # Récupère les catégories de techniques
    select = SkillCategorySelect(categories)
    view = View()
    view.add_item(select)

    embed = discord.Embed(title="Sélectionner une catégorie de techniques", description="Choisissez une catégorie pour voir les techniques disponibles.", color=0xFFBF66)
    await ctx.send(embed=embed, view=view)



@skills.command()
async def setup(ctx, mention: str = None, technique: str = None, palier: int = None):
    """
    Définit ou met à jour le palier d'une technique pour un utilisateur.
    Si l'utilisateur n'existe pas dans la base de données, il est initialisé.
    """
    if mention:
        # Extraire l'ID utilisateur de la mention (en enlevant les chevrons et '@')
        user_id = int(mention.strip('<@!>'))
    else:
        # Utiliser l'ID de l'auteur de la commande si aucune mention n'est fournie
        user_id = ctx.author.id

    palier_dict = {1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V', 6: 'X'}

    if palier not in palier_dict:
        await ctx.send("Palier invalide. Les paliers vont de 1 à 6.")
        return

    async with aiosqlite.connect('inventory.db') as db:
        # Vérifier si l'utilisateur existe
        cursor = await db.execute("SELECT * FROM skills WHERE user_id = ?", (user_id,))
        user_data = await cursor.fetchone()

        if user_data is None:
            # Si l'utilisateur n'existe pas dans la base, l'initialiser
            await db.execute("INSERT INTO skills (user_id) VALUES (?)", (user_id,))
            await db.commit()

        # Mettre à jour le palier de la technique
        technique_column = technique.lower().replace(" ", "_").replace("é", "e")  # Gérer les caractères spéciaux
        await db.execute(f"UPDATE skills SET {technique_column} = ? WHERE user_id = ?", (palier, user_id))
        await db.commit()

        await ctx.send(f"Le palier de la technique {technique} de {mention} a été mis à jour à {palier_dict[palier]}.")

@skills.command()
async def reset(ctx, mention: str = None, technique: str = None):
    """
    Réinitialise une technique pour un utilisateur en mettant son palier à 0.
    Si l'utilisateur n'existe pas dans la base de données, il est initialisé.
    """
    if not mention or not technique:
        await ctx.send("Veuillez mentionner un utilisateur et fournir le nom de la technique. Exemple : `?skills reset @utilisateur \"Nom de la Technique\"`")
        return

    try:
        # Extraire l'ID utilisateur de la mention (en enlevant les chevrons et '@')
        user_id = int(mention.strip('<@!>'))
    except ValueError:
        await ctx.send("La mention de l'utilisateur est invalide.")
        return

    # Trouver le nom de la colonne correspondant à la technique
    technique_column = technique_column_mapping.get(technique, technique.lower().replace(" ", "_").replace("é", "e"))

    if technique_column not in technique_column_mapping.values():
        await ctx.send(f"La technique '{technique}' est invalide ou non reconnue.")
        return

    async with aiosqlite.connect('inventory.db') as db:
        # Vérifier si l'utilisateur existe
        cursor = await db.execute("SELECT * FROM skills WHERE user_id = ?", (user_id,))
        user_data = await cursor.fetchone()

        if user_data is None:
            # Si l'utilisateur n'existe pas dans la base, l'initialiser
            await db.execute("INSERT INTO skills (user_id) VALUES (?)", (user_id,))
            await db.commit()

        # Réinitialiser le palier de la technique à 0
        await db.execute(f"UPDATE skills SET {technique_column} = 0 WHERE user_id = ?", (user_id,))
        await db.commit()

        await ctx.send(f"La technique '{technique}' de {mention} a été réinitialisée (Technique non apprise).")


# Dictionnaire des descriptions des techniques
technique_descriptions = {
    "Ittôryû": "Style d'épée à une seule lame.",
    "Nitôryû": "Style de combat avec deux épées.",
    "Santôryû": "Technique de combat à trois épées.",
    "Mûtôryû": "Style de combat sans épée.",
    "Style du Renard de Feu": "Un style basé sur la vitesse et la précision.",
    "Danse de l'Épée des Remous": "Une technique fluide et élégante.",
    "Style de Combat Tireur d'Élite": "Maîtrise des tirs de précision.",
    "Balle Explosive": "Une balle causant une explosion à l'impact.",
    "Balle Incendiaire": "Une balle qui s'enflamme à l'impact.",
    "Balle Fumigène": "Une balle qui libère de la fumée.",
    "Balle Dégoutante": "Une balle qui libère une odeur désagréable.",
    "Balle Cactus": "Une balle hérissée de piquants.",
    "Balle Venimeuse": "Une balle qui libère un poison.",
    "Balle Électrique": "Une balle électrifiée à l'impact.",
    "Balle Gelante": "Une balle qui gèle à l'impact.",
    "Green Pop": "Une technique utilisant des projectiles végétaux.",
    "Karaté": "Un art martial traditionnel.",
    "Taekwondo": "Un art martial focalisé sur les coups de pied.",
    "Judo": "Un art martial basé sur les projections.",
    "Boxe": "Un style de combat axé sur les coups de poing.",
    "Okama Kenpo": "Un style unique et excentrique.",
    "Hassoken": "Une technique rare basée sur des vibrations.",
    "Ryusoken": "Un style inspiré par les dragons.",
    "Jambe noire": "Un style de combat utilisant les jambes.",
    "Gyojin Karaté (simplifié)": "Une version simplifiée du karaté des hommes-poissons.",
    "Rope Action": "Un style basé sur l'utilisation de cordes.",
    "Ramen Kenpo": "Un style excentrique inspiré de la cuisine.",
    "Gyojin Karaté": "Le karaté des hommes-poissons.",
    "Art Martial Tontatta": "Un style d'art martial des Tontatta.",
    "Jao Kun Do": "Un style de combat rapide et flexible.",
    "Electro": "Une technique basée sur l'électricité.",
    "Sulong": "Un état spécial des Mink en pleine lune.",
    "Style Personnel": "Un style unique à son utilisateur."
}

# Fonction mise à jour pour afficher les descriptions
@skills.command()
async def info(ctx):
    """
    Affiche un menu déroulant pour sélectionner une catégorie de techniques.
    Lorsque l'utilisateur sélectionne une catégorie, les descriptions des techniques sont affichées.
    """
    categories = list(skills_liste.keys())
    select = SkillCategoryInfoSelect(categories)
    view = View()
    view.add_item(select)

    embed = discord.Embed(title="Sélectionner une catégorie de techniques", description="Choisissez une catégorie pour voir les descriptions des techniques.", color=0xFFBF66)
    await ctx.send(embed=embed, view=view)

class SkillCategoryInfoSelect(Select):
    def __init__(self, categories):
        options = [discord.SelectOption(label=category) for category in categories]
        super().__init__(placeholder="Choisissez une catégorie", options=options)

    async def callback(self, interaction: discord.Interaction):
        category = self.values[0]

        # Créer l'embed avec les descriptions des techniques
        embed = discord.Embed(title=f"Descriptions des techniques : {category}", color=0xFFBF66)
        
        for technique, _ in skills_liste[category].items():
            description = technique_descriptions.get(technique, "Description non disponible.")
            embed.add_field(name=technique, value=description, inline=False)

        await interaction.response.send_message(embed=embed)

@skills.command()
async def upgrade(ctx, technique_name: str):
    """
    Commande pour améliorer une technique spécifique avec un embed.
    La technique ne peut être améliorée que si elle est au minimum au palier 1.
    """
    user_id = ctx.author.id
    technique_column = technique_column_mapping.get(technique_name)
    
    if not technique_column:
        await ctx.send(f"La technique {technique_name} n'existe pas. Vérifiez le nom et réessayez.", ephemeral=True)
        return

    async with aiosqlite.connect('inventory.db') as db:
        # Récupération des points depuis `user_stats` et du palier actuel depuis `skills`
        cursor = await db.execute("""
            SELECT us.points, us.points_spent, s.{}
            FROM user_stats us
            LEFT JOIN skills s ON us.user_id = s.user_id
            WHERE us.user_id = ?
        """.format(technique_column), (user_id,))
        user_data = await cursor.fetchone()

        if not user_data:
            await ctx.send("Vous n'êtes pas enregistré dans la base de données. Veuillez essayer à nouveau après votre initialisation.", ephemeral=True)
            return

        points, points_spent, current_tier = user_data

        # Vérification si le palier est à 0, ce qui signifie que la technique n'est pas encore débloquée
        if current_tier == 0:
            embed = discord.Embed(title="Erreur d'Amélioration", description=f"Votre compétence {technique_name} est au palier 0 et ne peut pas être améliorée. Veuillez demander à un membre du staff de la configurer à un palier d'initiation (1).", color=0xFF0000)
            await ctx.send(embed=embed)
            return

        # Vérification si la compétence est déjà au niveau maximum
        if current_tier >= 6:
            embed = discord.Embed(title="Amélioration de Technique", description=f"Votre compétence {technique_name} est déjà au niveau maximum (X).", color=0xFFBF66)
            await ctx.send(embed=embed)
            return

        # Calcul du coût pour passer au palier suivant
        tier_cost = [0, 6, 12, 18, 24, 30]
        upgrade_cost = tier_cost[current_tier]

        if points < upgrade_cost:
            embed = discord.Embed(title="Amélioration de Technique", description=f"Vous n'avez pas assez de points pour améliorer {technique_name}.", color=0xFFBF66)
            embed.add_field(name="Points nécessaires", value=upgrade_cost, inline=True)
            embed.add_field(name="Points disponibles", value=points, inline=True)
            await ctx.send(embed=embed)
            return

        # Mise à jour des points et du niveau de compétence
        new_tier = current_tier + 1
        new_points = points - upgrade_cost
        new_points_spent = points_spent + upgrade_cost

        await db.execute(f"UPDATE skills SET {technique_column} = ? WHERE user_id = ?", (new_tier, user_id))
        await db.execute("UPDATE user_stats SET points = ?, points_spent = ? WHERE user_id = ?", (new_points, new_points_spent, user_id))
        await db.commit()

        # Embed de réponse avec succès
        embed = discord.Embed(title="Amélioration de Technique", description=f"Félicitations ! Votre compétence {technique_name} a été améliorée.", color=0xFFBF66)
        embed.add_field(name="Nouveau Palier", value=f"{['I', 'II', 'III', 'IV', 'V', 'X'][new_tier - 1]}", inline=True)
        embed.add_field(name="Points restants", value=new_points, inline=True)
        embed.add_field(name="Vôtre Elo", value=new_points_spent, inline=True)
        await ctx.send(embed=embed)

# Commande @bot.command() pour ?roll D
@bot.command()
async def roll(ctx, *, arg=None):
    if arg == "D":  # Vérifier que l'argument est bien "D"
        chance = random.randint(1, 15)  # Génère un nombre entre 1 et 10
        result = "D" if chance == 1 else "Pas D"  # Si c'est 1, alors c'est un "D"

        # Création de l'embed avec la couleur FFBF66
        embed = discord.Embed(
            title="Résultat du lancer de D",
            description=f"Tu as lancé le dé et tu as obtenu : **{result}**",
            color=0xFFBF66  # Couleur FFBF66
        )

        # Ajouter un GIF (remplacer l'URL par un GIF de One Piece en rapport avec le "D")
        embed.set_image(url="https://media.giphy.com/media/your-gif-url.gif")  # Remplacer par le lien réel du GIF

        # Envoi de l'embed
        await ctx.send(embed=embed)
    else:
        await ctx.send("Commande invalide. Utilise `?roll D` pour lancer le dé.")


fouille_cooldown = datetime.timedelta(hours=24)  # Cooldown de 24 heures
user_last_fouille = {}  # Dictionnaire pour stocker les derniers entraînements des utilisateurs

@bot.command(name="fouille")
async def fouille(ctx):
    """Permet aux utilisateurs de fouiller et de potentiellement obtenir des récompenses."""
    user_id = ctx.author.id
    guild = ctx.guild
    category_id = ctx.channel.category_id

    fiche_role = discord.utils.get(ctx.author.roles, id=1270083788529074220)
    
    if not fiche_role:
        embed = discord.Embed(
            title="Fiche non validée",
            description="Vous ne pouvez pas entraîner car votre fiche n'a pas encore été validée.",
            color=0xFF0000
        )
        await ctx.send(embed=embed)
        return

    current_time = datetime.datetime.now()
    last_fouille_time = user_last_fouille.get(ctx.author.id, datetime.datetime.fromtimestamp(0))

    if current_time - last_fouille_time < fouille_cooldown:
        remaining_time = fouille_cooldown - (current_time - last_fouille_time)
        hours, remainder = divmod(remaining_time.total_seconds(), 3600)
        minutes, _ = divmod(remainder, 60)
        time_left = f"{int(hours)} heures et {int(minutes)} minutes"
        
        embed = discord.Embed(
            title="Temps de cooldown",
            description=f"Vous devez attendre encore **{time_left}** avant de pouvoir entraîner cette capacité à nouveau.",
            color=0xFF0000
        )
        await ctx.send(embed=embed)
        return

    # Répartition des probabilités par défaut
    drops = [
        (20, "Rien"),
        (23, "Berry"),
        (23, "Coffre en bois"),
        (15, "Coffre en argent"),
        (10, "Coffre en or"),
        (6, "Parchemin Antique"),
        (1.5, "Fruit Paramecia/Zoan classique"),
        (1, "Fruit Zoan antique/Logia"),
        (0.5, "Fruit Zoan mythique")
    ]

    # Répartition spécifique pour la catégorie 1272046653116780574
    if category_id == 1272046653116780574:
        drops = [
            (23, "Rien"),
            (20, "Berry"),
            (14, "Coffre en bois"),
            (12, "Coffre en argent"),
            (10, "Coffre en or"),
            (8, "Parchemin Antique"),
            (10, "Dial"),
            (1.5, "Fruit Paramecia/Zoan classique"),
            (1, "Fruit Zoan antique/Logia"),
            (0.5, "Fruit Zoan mythique")
        ]

    # Fonction pour tirer un item au hasard
    def get_random_drop():
        total = sum(weight for weight, _ in drops)
        rand = random.uniform(0, total)
        upto = 0
        for weight, item in drops:
            if upto + weight >= rand:
                return item
            upto += weight
        return "Rien"

    reward = get_random_drop()

    embed = discord.Embed(color=0xFFBF66)

    # Message descriptif selon la récompense
    reward_message = {
        "Berry": "Tu as trouvé une somme impressionnante de Berry.",
        "Coffre en bois": "Tu as découvert un coffre en bois. Qui sait ce qu'il contient !",
        "Coffre en argent": "Un coffre en argent brillant se trouve dans tes mains.",
        "Coffre en or": "Félicitations, un coffre en or très rare est à toi !",
        "Parchemin Antique": "Un mystérieux parchemin antique a été trouvé.",
        "Dial": "Un Dial unique est maintenant en ta possession.",
        "Fruit Paramecia/Zoan classique": "Un fruit du démon intéressant t'attend.",
        "Fruit Zoan antique/Logia": "Un fruit du démon rare a été trouvé.",
        "Fruit Zoan mythique": "Un fruit mythique t'appartient désormais.",
        "Rien": "Malheureusement, tu n'as rien trouvé cette fois."
    }

    embed.title = f"Récompense trouvée - {reward}"
    embed.description = f"*{reward_message[reward]}*"

    # Ajouter des récompenses spécifiques
    if reward == "Berry":
        amount = random.randint(100000, 500000)
        embed.add_field(name="Récompense", value=f"-  **{amount} Berry 🪙**")
    elif reward == "Coffre en bois":
        berry_amount = random.randint(50000, 300000)
        lingots = ["Lingot de Fer"]
        lingots_count = {lingot: random.randint(3, 6) for lingot in lingots}
        lingots_str = "\n".join([f"-  **{count} {lingot} 💵**" for lingot, count in lingots_count.items()])
        embed.add_field(name="Récompense", value=f"-  **{berry_amount} Berry 🪙**\n{lingots_str}")
    elif reward == "Coffre en argent":
        berry_amount = random.randint(500000, 1000000)
        lingots = ["Lingot de Fer"]
        lingots_count = {lingot: random.randint(5, 8) for lingot in lingots}
        lingots_rare = random.choice(["Lingot de Titane 💷", "Lingot d'Or 💴"])
        lingots_str = "\n".join([f"-  **{count} {lingot} 💵**" for lingot, count in lingots_count.items()])
        embed.add_field(name="Récompense", value=f"-  **{berry_amount} Berry 🪙**\n{lingots_str}\n-  **1 {lingots_rare}**")
    elif reward == "Coffre en or":
        berry_amount = random.randint(1000000, 1500000)
        lingots = ["Lingot de Fer"]
        lingots_count = {lingot: random.randint(9, 12) for lingot in lingots}
        lingots_rare = random.choice(["Lingot de Titane 💷", "Lingot d'Or 💴"])
        gem = random.choice(["Diamant 💎", "Lingot de Granit Marin 💶"])
        lingots_str = "\n".join([f"-  **{count} {lingot} 💵**" for lingot, count in lingots_count.items()])
        embed.add_field(name="Récompense", value=f"-  **{berry_amount} Berry 🪙**\n{lingots_str}\n-  **1 {lingots_rare}**\n-  **1 {gem} **")
    elif reward == "Parchemin Antique":
        embed.add_field(name="Récompense", value="- 📜 **Parchemin Antique**")
    elif reward == "Dial":
        dial_types = [
            "Axe-Dial", "Eisen-Dial", "Breath-Dial", "Jet-Dial", "Heat-Dial", 
            "Flash-Dial", "Flavor-Dial", "Impact-Dial", "Lampe-Dial", 
            "Milky-Dial", "Reject-Dial", "Audio-Dial", "Hydro-Dial", "Thunder-Dial"
        ]
        dial = random.choice(dial_types)
        embed.add_field(name="Récompense", value=f"-  🐚  **Dial : {dial}**")
    elif "Fruit" in reward:
        # Logique pour gérer l'ajout d'un fruit du démon
        async with aiosqlite.connect('inventory.db') as db:
            # Liste des fruits disponibles à ajouter
            if reward == "Fruit Paramecia/Zoan classique":
                fruit_category = paramecias_corporel + paramecias_productif + paramecias_manipulateur + zoan_classique
            elif reward == "Fruit Zoan antique/Logia":
                fruit_category = zoan_antique + logia
            elif reward == "Fruit Zoan mythique":
                fruit_category = zoan_mythique
            else:
                fruit_category = []

            # Chercher les fruits non possédés par l'utilisateur
            query = f"""
                SELECT fdd_name FROM fdd_inventory
                WHERE fdd_name IN ({', '.join(['?'] * len(fruit_category))})
                AND user_id = ?
            """
            cursor = await db.execute(query, (*fruit_category, user_id))
            taken_fruits = [row[0] for row in await cursor.fetchall()]

            # Sélectionner un fruit disponible
            available_fruits = [fruit for fruit in fruit_category if fruit not in taken_fruits]
            
            if available_fruits:
                fruit = random.choice(available_fruits)
                try:
                    await db.execute(""" 
                        INSERT INTO fdd_inventory (user_id, fdd_name)
                        VALUES (?, ?)
                        ON CONFLICT(user_id, fdd_name) DO NOTHING
                    """, (user_id, fruit))
                    await db.commit()
                    embed.add_field(name="Récompense", value=f"- 🍇 **Fruit du Démon : {fruit}**")
                except Exception as e:
                    logging.error(f"Erreur lors de l'ajout du FDD : {e}")
                    embed.add_field(name="Récompense", value="- ❌ Impossible d'ajouter ce fruit.")
            else:
                embed.add_field(name="Récompense", value="- ❌ Aucun fruit disponible cette fois.")
    else:
        embed.add_field(name="Récompense", value="-  Rien trouvé cette fois. ❌")

    # Mise à jour du dernier moment de fouille
    user_last_fouille[ctx.author.id] = current_time

    await ctx.send(embed=embed)

# Charger les variables d'environnement du fichier .env
load_dotenv()

# Récupérer le token Discord
TOKEN = os.getenv("DISCORD_TOKEN")

# Exemple d'utilisation
print("Le token Discord est :", TOKEN)

keep_alive()
bot.run(TOKEN)
import asyncio
import aiosqlite
import datetime
import random
import logging
import discord
from discord.ext import commands
from discord import SelectOption, ui, Interaction, Embed
from discord.ui import Select, View
import os
from dotenv import load_dotenv
from keep_alive import keep_alive



logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


print("aiosqlite is installed and working!")

intents = discord.Intents().all()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='?', intents=intents)

elo_emoji = "<:Elo:1289528803462217748>"


@bot.event
async def on_ready():
    logging.info('Bot is ready.')

    async with aiosqlite.connect('inventory.db') as db:
        # Création des tables si elles n'existent pas déjà
        await db.execute('''CREATE TABLE IF NOT EXISTS user_stats (
            user_id INTEGER PRIMARY KEY,
            force INTEGER DEFAULT 5,
            vitesse INTEGER DEFAULT 5,
            resistance INTEGER DEFAULT 5,
            endurance INTEGER DEFAULT 5,
            agilite INTEGER DEFAULT 5,
            combat INTEGER DEFAULT 5,
            FDD INTEGER DEFAULT 0,
            haki_armement INTEGER DEFAULT 0,
            haki_observation INTEGER DEFAULT 0,
            haki_rois INTEGER DEFAULT 0,
            points INTEGER DEFAULT 0,
            points_spent INTEGER DEFAULT 0
        )''')
        await db.execute('''CREATE TABLE IF NOT EXISTS fdd_inventory (
            user_id INTEGER,
            fdd_name TEXT UNIQUE,
            description TEXT,
            eaten TEXT DEFAULT "False",
            PRIMARY KEY (user_id, fdd_name),
            FOREIGN KEY (user_id) REFERENCES user_stats (user_id)
        )''')
        await db.execute('''CREATE TABLE IF NOT EXISTS user_decorations (
            user_id INTEGER PRIMARY KEY,
            thumbnail_url TEXT,
            icon_url TEXT,
            main_url TEXT,
            color TEXT DEFAULT '#FFBF66',
            ost_url TEXT,
            FOREIGN KEY (user_id) REFERENCES user_stats (user_id)
        )''')
        await db.execute('''CREATE TABLE IF NOT EXISTS skills (
            user_id INTEGER,
            ittoryu INTEGER DEFAULT 0,
            nitoryu INTEGER DEFAULT 0,
            santoryu INTEGER DEFAULT 0,
            mutoryu INTEGER DEFAULT 0,
            style_du_renard_de_feu INTEGER DEFAULT 0,
            danse_de_lepee_des_remous INTEGER DEFAULT 0,
            style_de_combat_tireur_delite INTEGER DEFAULT 0,
            balle_explosive INTEGER DEFAULT 0,
            balle_incendiaire INTEGER DEFAULT 0,
            balle_fumigene INTEGER DEFAULT 0,
            balle_degoutante INTEGER DEFAULT 0,
            balle_cactus INTEGER DEFAULT 0,
            balle_venimeuse INTEGER DEFAULT 0,
            balle_electrique INTEGER DEFAULT 0,
            balle_gelante INTEGER DEFAULT 0,
            green_pop INTEGER DEFAULT 0,
            karate INTEGER DEFAULT 0,
            taekwondo INTEGER DEFAULT 0,
            judo INTEGER DEFAULT 0,
            boxe INTEGER DEFAULT 0,
            okama_kenpo INTEGER DEFAULT 0,
            hassoken INTEGER DEFAULT 0,
            ryusoken INTEGER DEFAULT 0,
            jambe_noire INTEGER DEFAULT 0,
            gyojin_karate_simplifie INTEGER DEFAULT 0,
            rope_action INTEGER DEFAULT 0,
            ramen_kenpo INTEGER DEFAULT 0,
            gyojin_karate INTEGER DEFAULT 0,
            art_martial_tontatta INTEGER DEFAULT 0,
            jao_kun_do INTEGER DEFAULT 0,
            electro INTEGER DEFAULT 0,
            sulong INTEGER DEFAULT 0,
            style_personnel INTEGER DEFAULT 0,
            FOREIGN KEY (user_id) REFERENCES user_stats (user_id)
        )''')
        await db.commit()

sabreur = {
    "Ittôryû": {
        "description": "Technique spéciale nécessitant l’usage d’un sabre. L'ittôryû est une compétence simple mais polyvalente, pouvant s’utiliser dans de nombreuses situations. Les techniques à un sabre sont des coups de lames renforcés, allant jusqu’à projeter des lames d’air tranchantes ou à trancher des matières solides comme du beurre. C’est une base primordiale pour les épéistes avant de créer leur style unique, ainsi que la source de nombreux dérivés."
    },
    "Nitôryû": {
        "description": "Dérivée de l'ittôryû, le style à deux sabres fonctionne de la même manière mais avec deux sabres pour des attaques offensives renforcées, allant jusqu'à de puissantes lames d’air. Ce style permet de combiner rapidité et puissance."
    },
    "Santôryû": {
        "description": "Le style du sabreur à trois sabres, généralement une limite technique pour la majorité des guerriers. Ceux qui maîtrisent ce style utilisent la troisième lame entre leurs dents, créant ainsi un style très agressif. Les attaques sont puissantes et peuvent créer des lames d’air distantes et puissantes. Toutefois, l’usage de ce style n’est pas recommandé pour une bonne hygiène dentaire."
    },
    "Mûtôryû": {
        "description": "Le style sans sabre, aussi appelé Mûtôryû, est assez particulier. Ce style ne renforce pas les lames, mais directement le corps de l’épéiste. Cela permet de créer des lames d’air avec des coups de bras ou d’autres parties du corps, imitant l’effet d’un sabre sans en posséder un."
    },
    "Style du Renard de Feu": {
        "description": "Développé à Wano Kuni, ce style flamboyant permet d'embraser sa lame et de trancher les flammes pour s’en protéger ou y créer des ouvertures. Bien que la création de flammes soit plus modeste que celle d’autres pouvoirs, ce style reste redoutable pour ses attaques offensives et sa capacité à se défendre contre le feu."
    },
    "Danse de l'Épée des Remous": {
        "description": "La danse de l’épée est une technique non-violente, visant à désarmer les adversaires plutôt qu’à les blesser. Le sabreur exécute une série de mouvements semblables à une danse, frappant les armes ennemies pour les faire tomber des mains de leurs porteurs."
    }
}

tireur = {
    "Style de Combat Tireur d'Élite": {
        "description": "Basé sur l’usage de projectiles et d’armes à feu, le tireur d’élite utilise des munitions spéciales modifiées pour s’adapter à toutes sortes de situations. Certaines de ces balles peuvent être renforcées par l’usage de Dials ou être personnalisées grâce à des techniques uniques. Les tireurs d’élite sont des experts dans l’usage des balles pour un maximum d’efficacité."
    },
    "Balle Explosive": {
        "description": "Balles couvertes ou contenant de la poudre à canon, ces balles explosent au contact d’une cible, provoquant des dégâts massifs à l'impact. Elles sont particulièrement efficaces contre les armures et les structures."
    },
    "Balle Incendiaire": {
        "description": "Ces balles s’enflamment par friction, créant une explosion de feu au moment du tir. Elles sont idéales pour enflammer une cible, déclencher des incendies ou brûler un adversaire sur place."
    },
    "Balle Fumigène": {
        "description": "Une balle contenant une poudre qui libère de la fumée au contact. Cela bloque la vue d’une ou plusieurs personnes, idéal pour aveugler un groupe d’adversaires ou créer des distractions. Cependant, elles sont vulnérables aux vents forts qui dispersent la fumée rapidement."
    },
    "Balle Dégoutante": {
        "description": "Plutôt que d'utiliser une balle classique, ce style utilise des projectiles répugnants : œufs pourris, balles recouvertes de crottes de pigeons, ou autres substances dégoûtantes. L’objectif est de perturber et de dégoûter l’adversaire, affectant souvent sa concentration ou son moral."
    },
    "Balle Cactus": {
        "description": "Au lieu d’une balle, un projectile à épines est lancé. Lorsqu’il explose, il libère plusieurs projectiles en forme de cactus, qui se plantent dans la peau de l’adversaire. Ces projectiles sont particulièrement douloureux et difficiles à enlever."
    },
    "Balle Venimeuse": {
        "description": "Ces balles contiennent des substances toxiques et dangereuses comme du poison ou des drogues. Elles peuvent affaiblir, empoisonner ou même tuer à petit feu l'adversaire si elles ne sont pas traitées à temps."
    },
    "Balle Électrique": {
        "description": "Les balles électriques fonctionnent comme un taser. Elles contiennent une petite batterie qui libère une décharge électrique au contact. Ces balles sont idéales pour paralyser une cible ou la neutraliser temporairement."
    },
    "Balle Gelante": {
        "description": "Ces balles contiennent de l'azote liquide ou d’autres substances permettant de geler instantanément la cible. Cela peut figer un membre ou même une partie du corps d’un ennemi, le rendant vulnérable aux attaques suivantes."
    },
    "Green Pop": {
        "description": "Ces balles contiennent des germes et des graines provenant du Nouveau Monde. Lorsqu’elles touchent une cible, elles germent et poussent en quelques secondes, créant des racines ou des plantes agressives. Ces plantes peuvent immobiliser, empoisonner ou causer des dommages physiques avec leurs épines et autres mécanismes."
    }
}

arts = {
    "Karaté": {
        "description": "Utilisant le corps de l’homme comme arme mêlant des mouvements offensifs comme défensifs tout en développant le bien-être de l’esprit."
    },
    "Taekwondo": {
        "description": "Style à percussion utilisant pieds et poings, le Taekwondo vise essentiellement entre la ceinture et le visage pour des coups impactants et rapides."
    },
    "Judo": {
        "description": "Le judo est un style de combat rapproché maximisant les contacts corporels pour projeter ou plaquer la cible au sol par l’usage de nombreuses prises utilisant l’entièreté du corps."
    },
    "Boxe": {
        "description": "Libre à nombreux dérivés, la boxe dans son état global consiste en un enchaînement de frappes puissantes vers le haut du corps et essentiellement le visage."
    }
}
  
combattant = {
    "Okama Kenpo": {
        "description": "Semblable à une danse de ballet, l’Okama Kenpo est un style reposant sur les coups de pieds et de jambes agiles, rapides et puissants. Une fois la fierté mise de côté, ce style est redoutable."
    },
    "Hassoken": {
        "description": "Art martial redoutablement fort originaire du pays des fleurs, le Hassoken est un style de combat brutal et impactant visant à créer des vibrations par les coups employés pour percer les défenses."
    },
    "Ryusoken": {
        "description": "Aussi appelé griffe du dragon, le Ryusoken est un art basé sur l’usage des mains comme des griffes de dragons pour écraser ses cibles avec une forte poigne, offrant une puissance destructrice à l’offensive, bien que difficile à diriger."
    },
    "Jambe noire": {
        "description": "Développé par des pirates cuisiniers, ce style permet de se battre en n’utilisant que ses jambes pour préserver l’état des mains. Ce style de coups de jambes permet une grande mobilité ainsi que des attaques destructrices et rapides. Maîtrisé à haut niveau, les experts peuvent faire usage du style de la Jambe du diable, une évolution de la jambe noire combinant la force des jambes avec une extrême chaleur corporelle, enflammant la jambe par la friction et la vitesse."
    },
    "Gyojin Karaté (simplifié)": {
        "description": "Adaptation du style des hommes poissons aux combattants terrestres, cette forme du Gyojin karaté permet des frappes offensives et défensives très puissantes."
    }
}

uniques = {
    "Rope Action": {
        "description": "Style de combat basé sur l’usage de câbles longs servant à l'attache des navires ou d’autres matériaux maritimes, visant à ligoter la cible avec puissance."
    },
    "Ramen Kenpo": {
        "description": "Utilisant nouilles et farine, le Ramen Kenpo est un art peu célèbre et complexe utilisant des nouilles pour se battre comme des armes ou comme armure. Pratique pour limiter les mouvements et immobiliser une cible, mais peu efficace face aux épéistes."
    },
    "Gyojin Karaté": {
        "description": "Style de combat similaire au karaté terrien, cet art utilise le corps de son utilisateur pour des mouvements de frappe offensifs comme défensifs. Au-delà de permettre aux hommes poissons des attaques puissantes et brutales, cet art permet aussi de manipuler l’eau environnante pour diriger des vagues ou des balles d’eau vers l'ennemi. Plus il y a d’eau à proximité, plus l’utilisateur sera redoutable, obtenant le plein potentiel de ce style lorsqu’il se bat en pleine mer."
    },
    "Art Martial Tontatta": {
        "description": "Basé sur l’usage de la force exceptionnelle de ces petits êtres, ce style offensif vise en premier temps à retirer ou arracher les vêtements de la cible pour la déconcentrer ou bien l'immobiliser avant de la frapper fort dans le but d’endormir ou de détruire."
    },
    "Jao Kun Do": {
        "description": "Ce style utilise les jambes étirées des longues jambes pour frapper avec la force de l’acier et maintenir l’adversaire à une certaine distance tout en attaquant. Mobile et puissant, ce n’est pas un style à sous-estimer."
    },
    "Electro": {
        "description": "Comme son nom l’indique, il s’agit ici d’une technique offensive visant à libérer de l’électricité sur l’adversaire grâce à la constitution biologique étrange des Minks, capables de produire facilement de l’électricité. Tous les Minks en sont capables, même les plus jeunes."
    },
    "Sulong": {
        "description": "Sous la lueur d’une pleine lune, les Minks les plus puissants obtiennent une nouvelle forme aussi imposante que destructrice. Sous cette forme, les yeux de l'individu changent, ses poils poussent énormément en prenant une couleur blanche, mais surtout leurs tailles et toutes leurs compétences physiques augmentent radicalement. Cependant, sous cette forme, la raison est mise de côté, laissant les individus se faire guider par l’instinct sauvage."
    }
}

perso = {
    "Style Personnel": {
        "description": "Pirates libres comme l’air ou marines et révolutionnaires voulant se démarquer des autres, il est normal d’avoir envie de créer un style de combat unique à soi-même, un art adapté parfaitement à nos compétences et nos besoins. Cela est possible, que ce soit en partant de rien ou en se basant sur d’autres styles de combats, mais cela demande de l'intelligence et de l’entraînement ! Pour ce faire, il faudra simplement voir les membres du staff en ticket et leur présenter sous une fiche votre style."
    }
}

# Dictionnaires des techniques pour chaque catégorie
skills_liste = {
    "Sabreur": sabreur,
    "Tireur": tireur,
    "Arts Martiaux": arts,
    "Combattant": combattant,
    "Uniques": uniques,
    "Personnel": perso
}


@bot.command()
async def setup(ctx, user: discord.User):
    # Vérifie si l'utilisateur a le rôle de staff (modérateur ou administrateur)
    if not any(role.id in STAFF_ROLES_IDS for role in ctx.author.roles):
        await ctx.send("Tu n'as pas les permissions nécessaires pour utiliser cette commande.")
        return

    # Récupérer l'ID de l'utilisateur mentionné
    user_id = user.id

    retries = 3  # Nombre de tentatives en cas de verrouillage
    for attempt in range(retries):
        try:
            # Connexion à la base de données avec gestion du verrouillage
            async with aiosqlite.connect('inventory.db') as db:
                # Liste des catégories de techniques
                categories = ["Sabreur", "Tireur", "Arts Martiaux", "Combattant", "Uniques", "Personnel"]

                for category in categories:
                    # Récupérer toutes les techniques pour cette catégorie
                    skills = skills_liste.get(category)
                    if skills:
                        for skill_name in skills:
                            # Vérifie si la technique existe pour l'utilisateur
                            cursor = await db.execute('SELECT palier FROM skills_stats WHERE user_id = ? AND skills_name = ?', (user_id, skill_name))
                            skill = await cursor.fetchone()

                            if not skill:
                                # Si la technique n'existe pas pour l'utilisateur, on l'ajoute avec palier 0
                                await db.execute('INSERT INTO skills_stats (user_id, skills_name, palier) VALUES (?, ?, ?)', (user_id, skill_name, 0))
                            else:
                                # Sinon, on met simplement le palier à 0
                                await db.execute('UPDATE skills_stats SET palier = 0 WHERE user_id = ? AND skills_name = ?', (user_id, skill_name))

                await db.commit()
            await ctx.send(f"Toutes les techniques de {user.name} ont été initialisées à palier 0.")
            return  # Si l'opération est réussie, on sort de la boucle

        except aiosqlite.DatabaseError as e:
            if attempt < retries - 1:
                await asyncio.sleep(2)  # Attendre 2 secondes avant de réessayer
                continue  # Réessayer l'opération
            else:
                await ctx.send("Une erreur est survenue en accédant à la base de données, essaye de réessayer plus tard.")
                print(f"Erreur de base de données: {e}")
                return

@bot.command(name='edit')
async def edit(ctx, edit_type: str, value: str):
    # Vérification du type d'édition
    if edit_type not in ["thumbnail", "icon", "main", "color", "ost"]:
        await ctx.send("Veuillez spécifier le type à éditer: `thumbnail`, `icon`, `main`, `color` ou `ost`.")
        return

    # Validation de l'URL ou couleur
    if edit_type in ["thumbnail", "icon", "main", "ost"]:
        if not (value.startswith("http://") or value.startswith("https://")):
            await ctx.send("Veuillez fournir une URL valide.")
            return
    if edit_type == "color":
        if not (value.startswith("#") and len(value) in [4, 7]):
            await ctx.send("Veuillez fournir une couleur valide au format HEX (par exemple, `#FFBF66`).")
            return
    if edit_type == "ost":
        if "youtube.com" not in value and "youtu.be" not in value:
            await ctx.send("Veuillez fournir une URL YouTube valide pour l'OST.")
            return

    # Choix de la colonne en fonction du type
    column = {
        "thumbnail": "thumbnail_url",
        "icon": "icon_url",
        "main": "main_url",
        "color": "color",
        "ost": "ost_url"
    }[edit_type]

    async with aiosqlite.connect('inventory.db') as db:
        try:
            # Mise à jour ou insertion des personnalisations
            await db.execute(f'''
                INSERT INTO user_decorations (user_id, {column})
                VALUES (?, ?)
                ON CONFLICT(user_id) DO UPDATE SET {column} = excluded.{column}
            ''', (ctx.author.id, value))
            await db.commit()
            await ctx.send(f"{edit_type.capitalize()} mis à jour avec succès ! Elle apparaîtra dans votre commande `?stats`.")
        except Exception as e:
            logging.error(f"Erreur lors de la mise à jour de {edit_type} pour l'utilisateur {ctx.author.id}: {e}")
            await ctx.send("Une erreur est survenue lors de la mise à jour.")

@bot.command(name='stats')
async def stats(ctx, member: discord.Member = None):
    target_member = member or ctx.author
    logging.info(f"Fetching stats for user: {target_member.id}")

    async with aiosqlite.connect('inventory.db') as db:
        try:
            async with db.execute('SELECT * FROM user_stats WHERE user_id = ?', (target_member.id,)) as cursor:
                stats = await cursor.fetchone()

            if not stats:
                logging.debug(f"Aucune stats trouvée pour l'utilisateur {target_member.id}. Création d'une nouvelle entrée.")
                await db.execute('INSERT INTO user_stats (user_id) VALUES (?)', (target_member.id,))
                await db.commit()
                stats = (target_member.id, 5, 5, 5, 5, 5, 5, 0, 0, 0, 0, 0, 0)

            (user_id, force, vitesse, resistance, endurance, agilite, combat, FDD, haki_armement, haki_observation, haki_rois, points, points_spent) = stats

            async with db.execute('SELECT thumbnail_url, icon_url, main_url, color, ost_url FROM user_decorations WHERE user_id = ?', (target_member.id,)) as cursor:
                decorations = await cursor.fetchone()

            if decorations:
                thumbnail_url, icon_url, main_url, color_hex, ost_url = decorations
                # Convertit la couleur en entier si elle est fournie sous forme hexadécimale
                color = int(color_hex.lstrip('#'), 16) if color_hex else 0xFFBF66
            else:
                thumbnail_url, icon_url, main_url, color, ost_url = (None, None, None, 0xFFBF66, None)

            embed = discord.Embed(
                title=f"Statistiques de {target_member.display_name}", 
                color=color,
                description=(
                    f"**Points disponibles : {points}**\n"
                    f"**Elo : {points_spent}**\n\n"
                    f"**╔═══════════ ∘◦ ✾ ◦∘ ════════════╗**\n\n"
                    f"**💪 ・ Force**: ➠ {force}%\n"
                    f"**🦵 ・ Vitesse**: ➠ {vitesse}%\n"
                    f"**🛡️ ・ Résistance**: ➠ {resistance}%\n"
                    f"**🫁 ・ Endurance**: ➠ {endurance}%\n"
                    f"**🤸‍♂️ ・ Agilité**: ➠ {agilite}%\n\n"
                    f"**════════════ ∘◦ ⛧ﾐ ◦∘ ════════════**\n\n"
                    f"**🥊 ・ Maîtrise de combat**: ➠ {combat}%\n"
                    f"**🍇 ・ Maîtrise de Fruit du démon**: ➠ {FDD}%\n\n"
                    f"**════════════ ∘◦ ⛧ﾐ ◦∘ ════════════**\n\n"
                    f"**🦾 ・ Haki de l'armement**: ➠ {haki_armement}%\n"
                    f"**👁️ ・ Haki de l'observation**: ➠ {haki_observation}%\n"
                    f"**👑 ・ Haki des Rois**: ➠ {haki_rois}%\n\n"
                    f"**╚═══════════ ∘◦ ❈ ◦∘ ════════════╝**"
                )
            )

            if thumbnail_url:
                embed.set_thumbnail(url=thumbnail_url)
            if icon_url:
                embed.set_author(name=target_member.display_name, icon_url=icon_url)
            if main_url:
                embed.set_image(url=main_url)
            if ost_url:
                embed.add_field(name="OST", value=f"[Cliquez ici pour écouter]({ost_url})", inline=False)

            await ctx.send(embed=embed)
        except Exception as e:
            logging.error(f"Erreur lors de la récupération des stats: {e}")
            await ctx.send("Une erreur est survenue lors de la récupération des statistiques.")
        
train_cooldown = datetime.timedelta(hours=24)  # Cooldown de 24 heures
user_last_train = {}  # Dictionnaire pour stocker les derniers entraînements des utilisateurs

@bot.command(name='train')
async def train(ctx):
    fiche_role = discord.utils.get(ctx.author.roles, id=1270083788529074220)
    
    if not fiche_role:
        embed = discord.Embed(
            title="Fiche non validée",
            description="Vous ne pouvez pas entraîner car votre fiche n'a pas encore été validée.",
            color=0xFF0000
        )
        await ctx.send(embed=embed)
        return

    current_time = datetime.datetime.now()
    last_train_time = user_last_train.get(ctx.author.id, datetime.datetime.fromtimestamp(0))

    if current_time - last_train_time < train_cooldown:
        remaining_time = train_cooldown - (current_time - last_train_time)
        hours, remainder = divmod(remaining_time.total_seconds(), 3600)
        minutes, _ = divmod(remainder, 60)
        time_left = f"{int(hours)} heures et {int(minutes)} minutes"
        
        embed = discord.Embed(
            title="Temps de cooldown",
            description=f"Vous devez attendre encore **{time_left}** avant de pouvoir entraîner cette capacité à nouveau.",
            color=0xFF0000
        )
        await ctx.send(embed=embed)
        return

    await ctx.send("Écrivez un message pour l'entraînement (minimum 150 caractères)")

    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel

    try:
        message = await bot.wait_for('message', check=check, timeout=300)  # 5 minutes pour répondre
    except asyncio.TimeoutError:
        await ctx.send("Vous n'avez pas répondu à temps.")
        return

    message_length = len(message.content)
    
    # Vérification du minimum de 150 caractères
    if message_length < 150:
        await ctx.send("Votre message doit contenir au moins 150 caractères pour valider l'entraînement.")
        return
    
    # Points en fonction de la longueur du message
    if message_length < 500:
        points_gagnes = random.choice([4, 5])
    elif 500 <= message_length <= 1000:
        points_gagnes = random.choice([5, 6])
    else:
        points_gagnes = random.choice([6, 7])
    
    # Ajout d'un point pour les boosters
    booster_role = discord.utils.get(ctx.guild.roles, id=1286757193651322971)
    if booster_role in ctx.author.roles:
        points_gagnes += 1

    # Sauvegarder les points gagnés
    async with aiosqlite.connect('inventory.db') as db:
        async with db.execute('SELECT points FROM user_stats WHERE user_id = ?', (ctx.author.id,)) as cursor:
            result = await cursor.fetchone()
            current_points = result[0] if result else 0

        new_points = current_points + points_gagnes
        await db.execute('UPDATE user_stats SET points = ? WHERE user_id = ?', (new_points, ctx.author.id))
        await db.commit()

    user_last_train[ctx.author.id] = current_time

    embed = discord.Embed(
        title="Entraînement terminé",
        description=f"Vous avez gagné {points_gagnes} points d'entraînement.",
        color=0xFFBF66
    )
    await ctx.send(embed=embed)


@bot.command(name='points')
async def points(ctx, action: str, amount: int, member: discord.Member = None):
    allowed_role_ids = [1269837965446610985, 1269838005234044958]  # Remplace par l'ID correct

    # Vérification si l'utilisateur possède le rôle admin
    admin_role = discord.utils.get(ctx.author.roles, id=allowed_role_ids)
    if not any(role.id in allowed_role_ids for role in ctx.author.roles):
        await ctx.send("Vous n'avez pas la permission d'utiliser cette commande.")
        return

    if action not in ['add', 'remove']:
        await ctx.send("Utilisez `add` pour ajouter des points ou `remove` pour en retirer.")
        return

    if amount <= 0:
        await ctx.send("La quantité de points doit être positive.")
        return

    member = member or ctx.author

    async with aiosqlite.connect('inventory.db') as db:
        async with db.execute('SELECT points FROM user_stats WHERE user_id = ?', (member.id,)) as cursor:
            result = await cursor.fetchone()
            current_points = result[0] if result else 0

        if action == 'add':
            new_points = current_points + amount
        elif action == 'remove':
            new_points = max(0, current_points - amount)

        await db.execute('UPDATE user_stats SET points = ? WHERE user_id = ?', (new_points, member.id))
        await db.commit()

        embed = discord.Embed(
        title="Points mis à jour",
        description=f"{amount} points {action}. Les points de {member.mention} sont déormais à {new_points} .",
        color=0xFFBF66
        )
        await ctx.send(embed=embed)

@bot.command(name='elo')
async def points(ctx, action: str, amount: int, member: discord.Member = None):
    allowed_role_ids = [1269837965446610985, 1269838005234044958]  # Remplace par l'ID correct

    # Vérification si l'utilisateur possède le rôle admin
    admin_role = discord.utils.get(ctx.author.roles, id=allowed_role_ids)
    if not any(role.id in allowed_role_ids for role in ctx.author.roles):
        await ctx.send("Vous n'avez pas la permission d'utiliser cette commande.")
        return

    if action not in ['add', 'remove']:
        await ctx.send("Utilisez `add` pour ajouter des points ou `remove` pour en retirer.")
        return

    if amount <= 0:
        await ctx.send("La quantité de points d'Elo doit être positive.")
        return

    member = member or ctx.author

    async with aiosqlite.connect('inventory.db') as db:
        async with db.execute('SELECT points_spent FROM user_stats WHERE user_id = ?', (member.id,)) as cursor:
            result = await cursor.fetchone()
            current_points = result[0] if result else 0

        if action == 'add':
            new_points = current_points + amount
        elif action == 'remove':
            new_points = max(0, current_points - amount)

        await db.execute('UPDATE user_stats SET points_spent = ? WHERE user_id = ?', (new_points, member.id))
        await db.commit()

        embed = discord.Embed(
        title="Points mis à jour",
        description=f"{amount} Elo {action}. L'Elo de {member.mention} est déormais à {new_points} .",
        color=0xFFBF66
        )
        await ctx.send(embed=embed)


@bot.command(name="upgrade")
async def upgrade(ctx):
    async with aiosqlite.connect('inventory.db') as db:
        # Récupérer les statistiques actuelles et les points disponibles
        async with db.execute('SELECT points, points_spent, force, resistance, endurance, vitesse, agilite, combat, FDD, haki_armement, haki_observation, haki_rois FROM user_stats WHERE user_id = ?', (ctx.author.id,)) as cursor:
            result = await cursor.fetchone()

        if result is None:
            await ctx.send("Aucune donnée trouvée pour cet utilisateur.")
            return

        points, points_spent, force, resistance, endurance, vitesse, agilite, combat, FDD, haki_armement, haki_observation, haki_rois = result

        # Récupérer les rôles de l'utilisateur pour vérifier le rôle FDD
        fdd_role_id = 1269823257079447623  # Remplacez par l'ID réel du rôle FDD
        hda_role_id = 1269823110958415934  # Remplacez par l'ID réel du rôle HDA
        hdo_role_id = 1269823083519279155  # Remplacez par l'ID réel du rôle HDO
        hdr_role_id = 1269823037830856744  # Remplacez par l'ID réel du rôle HDR

        has_fdd_role = discord.utils.get(ctx.author.roles, id=fdd_role_id) is not None
        has_hda_role = discord.utils.get(ctx.author.roles, id=hda_role_id) is not None
        has_hdo_role = discord.utils.get(ctx.author.roles, id=hdo_role_id) is not None
        has_hdr_role = discord.utils.get(ctx.author.roles, id=hdr_role_id) is not None


        # Création du menu déroulant
        select = Select(
            placeholder="Choisissez une statistique à améliorer...",
            options=[
                SelectOption(label="💪 Force", description=f"Améliorer Force (Actuel: {force}%)"),
                SelectOption(label="🛡️ Résistance", description=f"Améliorer Résistance (Actuel: {resistance}%)"),
                SelectOption(label="🫁 Endurance", description=f"Améliorer Endurance (Actuel: {endurance}%)"),
                SelectOption(label="🦵 Vitesse", description=f"Améliorer Vitesse (Actuel: {vitesse}%)"),
                SelectOption(label="🤸‍♂️ Agilité", description=f"Améliorer Agilité (Actuel: {agilite}%)"),
                SelectOption(label="🥊 Combat", description=f"Améliorer Combat (Actuel: {combat}%)"),
                SelectOption(label="🍇 FDD", description=f"Améliorer FDD (Actuel: {FDD}%)"),
                SelectOption(label="🦾 HDA", description=f"Débloquer/Améliorer HDA (Actuel: {haki_armement}%)"),
                SelectOption(label="👁️ HDO", description=f"Débloquer/Améliorer HDO (Actuel: {haki_observation}%)"),
                SelectOption(label="👑 HDR", description=f"Débloquer/Améliorer HDR (Actuel: {haki_rois}%)"),
            ]
        )

        async def select_callback(interaction):
            async with aiosqlite.connect('inventory.db') as db:
                # Mettre à jour les points et statistiques avant chaque interaction
                async with db.execute('SELECT points, points_spent, force, resistance, endurance, vitesse, agilite, combat, FDD, haki_armement, haki_observation, haki_rois FROM user_stats WHERE user_id = ?', (ctx.author.id,)) as cursor:
                    updated_result = await cursor.fetchone()

                points, points_spent, force, resistance, endurance, vitesse, agilite, combat, FDD, haki_armement, haki_observation, haki_rois = updated_result

                chosen_stat = select.values[0]

                stat_map = {
                    "💪 Force": "force",
                    "🛡️ Résistance": "resistance",
                    "🫁 Endurance": "endurance",
                    "🦵 Vitesse": "vitesse",
                    "🤸‍♂️ Agilité": "agilite",
                    "🥊 Combat": "combat",
                    "🍇 FDD": "FDD",
                    "🦾 HDA": "haki_armement",
                    "👁️ HDO": "haki_observation",
                    "👑 HDR": "haki_rois"
                }

                stat_col = stat_map.get(chosen_stat)

                if not stat_col:
                    embed = Embed(
                        title="Erreur",
                        description="Statistique sélectionnée invalide.",
                        color=0xFFBF66
                    )
                    await interaction.response.send_message(embed=embed)
                    return

                # Vérifier les conditions Elo pour Haki et FDD
                if stat_col == "haki_armement" and not (points_spent >= 500 or has_hda_role and points_spent >= 250):
                    embed = Embed(
                        title="Condition non remplie",
                        description="Vous devez avoir 500 Elo ou le rôle HDA et minimum 250 Elo pour améliorer Haki de l'Armement.",
                        color=0xFFBF66
                    )
                    await interaction.response.send_message(embed=embed)
                    return
                elif stat_col == "haki_observation" and not (points_spent >= 500 or has_hdo_role and points_spent >= 250):
                    embed = Embed(
                        title="Condition non remplie",
                        description="Vous devez avoir 500 Elo ou le rôle HDO et minimum 250 Elo pour améliorer Haki de l'Observation.",
                        color=0xFFBF66
                    )
                    await interaction.response.send_message(embed=embed)
                    return
                elif stat_col == "haki_rois" and not (points_spent >= 1000 or has_hdr_role and points_spent >= 500):
                    embed = Embed(
                        title="Condition non remplie",
                        description="Vous avez besoin d'au moins 1000 Elo ou le rôle HDR et 500 Elo pour améliorer Haki des Rois.",
                        color=0xFFBF66
                    )
                    await interaction.response.send_message(embed=embed)
                    return
                elif stat_col == "FDD" and not has_fdd_role:
                    embed = Embed(
                        title="Condition non remplie",
                        description="Vous avez besoin du rôle FDD pour améliorer cette statistique.",
                        color=0xFFBF66
                    )
                    await interaction.response.send_message(embed=embed)
                    return

                # Récupérer la valeur actuelle de la statistique choisie
                stats = {
                    "force": force,
                    "resistance": resistance,
                    "endurance": endurance,
                    "vitesse": vitesse,
                    "agilite": agilite,
                    "combat": combat,
                    "FDD": FDD,
                    "haki_armement": haki_armement,
                    "haki_observation": haki_observation,
                    "haki_rois": haki_rois
                }

                current_stat = stats.get(stat_col)

                if current_stat is None:
                    embed = Embed(
                        title="Erreur",
                        description="Erreur de récupération des données.",
                        color=0xFFBF66
                    )
                    await interaction.response.send_message(embed=embed)
                    return

                # Calcul des points requis
                if current_stat < 50:
                    points_needed = 4 if stat_col in ["force", "resistance", "endurance", "vitesse", "agilite"] else 10 if stat_col in ["combat", "FDD"] else 14 if stat_col in ["haki_armement", "haki_observation"] else 18
                elif current_stat < 100:
                    points_needed = 8 if stat_col in ["force", "resistance", "endurance", "vitesse", "agilite"] else 14 if stat_col in ["combat", "FDD"] else 18 if stat_col in ["haki_armement", "haki_observation"] else 22
                elif current_stat < 150:
                    points_needed = 12 if stat_col in ["force", "resistance", "endurance", "vitesse", "agilite"] else 18 if stat_col in ["combat", "FDD"] else 22 if stat_col in ["haki_armement", "haki_observation"] else 26
                else:
                    points_needed = 16 if stat_col in ["force", "resistance", "endurance", "vitesse", "agilite"] else 22 if stat_col in ["combat", "FDD"] else 26 if stat_col in ["haki_armement", "haki_observation"] else 30

                # Vérification des points
                if points >= points_needed:
                    # Mise à jour de la statistique
                    new_stat = current_stat + 5
                    update_query = f"UPDATE user_stats SET {stat_col} = ? WHERE user_id = ?"
                    await db.execute(update_query, (new_stat, ctx.author.id))
                    await db.commit()

                    # Mise à jour des points
                    new_points = points - points_needed
                    await db.execute("UPDATE user_stats SET points = ?, points_spent = ? WHERE user_id = ?", (new_points, points_spent + points_needed, ctx.author.id))
                    await db.commit()

                    # Envoi du message de confirmation
                    embed = Embed(
                        title="Amélioration réussie",
                        description=f"Votre {chosen_stat} est maintenant à {new_stat}%. Il vous reste {new_points} points.",
                        color=0xFFBF66
                    )
                    await interaction.response.send_message(embed=embed)
                else:
                    embed = Embed(
                        title="Points insuffisants",
                        description=f"Vous avez besoin de {points_needed} points pour améliorer cette statistique.",
                        color=0xFFBF66
                    )
                    await interaction.response.send_message(embed=embed)

        select.callback = select_callback
        view = View()
        view.add_item(select)


        # Envoyer le menu déroulant avec embed
        embed = Embed(
            title="Amélioration des Statistiques",
            description=f"Vous avez actuellement **{points} points** et **{points_spent} Elo**. Choisissez une statistique à améliorer :",
            color=0xFFBF66
        )
        await ctx.send(embed=embed, view=view)

@bot.command(name="nerf")
async def nerf(ctx, stat: str, percentage: int, member: discord.Member):
    allowed_role_ids = [1269837965446610985, 1269838005234044958]  # Remplace par l'ID correct
    # Vérification si l'utilisateur possède le rôle admin
    admin_role = discord.utils.get(ctx.author.roles, id=allowed_role_ids)
    if not any(role.id in allowed_role_ids for role in ctx.author.roles):
        await ctx.send("Vous n'avez pas la permission d'utiliser cette commande.")
        return
    
    if stat.lower() not in ["force", "resistance", "endurance", "vitesse", "agilite", "combat", "FDD", "haki_armement", "haki_observation", "haki_rois"]:
        await ctx.send(f"La statistique '{stat}' est invalide.")
        return

    async with aiosqlite.connect('inventory.db') as db:
        async with db.execute(f'SELECT {stat.lower()} FROM user_stats WHERE user_id = ?', (member.id,)) as cursor:
            result = await cursor.fetchone()

        if result is None:
            await ctx.send(f"Aucune donnée trouvée pour l'utilisateur {member.display_name}.")
            return

        current_value = result[0]

        # Calcul du nouveau pourcentage
        new_value = max(0, current_value - percentage)

        # Mise à jour de la statistique dans la base de données
        await db.execute(f'UPDATE user_stats SET {stat.lower()} = ? WHERE user_id = ?', (new_value, member.id))
        await db.commit()

    await ctx.send(f"La statistique **{stat}** de {member.mention} a été réduite de {percentage}%. Elle est maintenant à {new_value}%.")


@bot.command(name="top")
async def top(ctx, page: int = 1):
    fiche_role_id = 1270083788529074220  # Remplace avec l'ID réel du rôle Fiche validée
    print("Commande ?top déclenchée.")
    
    role_fiche = discord.utils.get(ctx.guild.roles, id=fiche_role_id)
    if role_fiche is None:
        print("Le rôle Fiche validée est introuvable.")
        await ctx.send("Le rôle Fiche validée n'existe pas sur ce serveur.")
        return
    
    print("Rôle Fiche validée trouvé.")
    
    # Connexion à la base de données
    async with aiosqlite.connect('inventory.db') as db:
        print("Connexion à la base de données réussie.")
        async with db.execute('''
            SELECT user_id, points_spent
            FROM user_stats
            ORDER BY points_spent DESC
        ''') as cursor:
            all_users = await cursor.fetchall()
            print(f"Nombre d'utilisateurs récupérés depuis la base de données : {len(all_users)}")

    # Récupérer directement les membres ayant le rôle "Fiche validée"
    valid_users = []
    for user_id, points_spent in all_users:
        try:
            member = await ctx.guild.fetch_member(user_id)  # Récupérer directement le membre depuis l'API
            if role_fiche in member.roles:
                print(f"L'utilisateur {member.display_name} a le rôle Fiche validée.")
                valid_users.append((member, points_spent))
            else:
                print(f"L'utilisateur {member.display_name} n'a pas le rôle Fiche validée.")
        except discord.NotFound:
            print(f"Utilisateur introuvable : {user_id}")
        except discord.Forbidden:
            print(f"Accès refusé pour l'utilisateur : {user_id}")

    print(f"Nombre d'utilisateurs avec le rôle Fiche validée : {len(valid_users)}")
    
    if not valid_users:
        await ctx.send("Aucun utilisateur avec le rôle Fiche validée n'a été trouvé.")
        return

    # Pagination (10 utilisateurs par page)
    users_per_page = 10
    total_pages = (len(valid_users) - 1) // users_per_page + 1
    print(f"Total de pages : {total_pages}")

    if page < 1 or page > total_pages:
        print(f"Page {page} invalide.")
        await ctx.send(f"Page invalide. Veuillez entrer un nombre de page entre 1 et {total_pages}.")
        return

    start_index = (page - 1) * users_per_page
    end_index = start_index + users_per_page
    users_on_page = valid_users[start_index:end_index]

    # Créer l'embed de classement
    embed = discord.Embed(title=f"Classement Elo (Page {page}/{total_pages})", color=0xFFBF66)
    for rank, (member, points_spent) in enumerate(users_on_page, start=start_index + 1):
        embed.add_field(name=f"{rank}/ {member.display_name}", value=f"***{elo_emoji} Elo: {points_spent} \n\n***", inline=False)
    
    print(f"Affichage des utilisateurs sur la page {page}.")
    
    # Ajouter une note pour la pagination
    embed.set_footer(text=f"Page {page}/{total_pages} • Utilisez ?top <numéro de page> pour naviguer.")

    await ctx.send(embed=embed)
    print("Classement envoyé.")



@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Désolé, cette commande n'existe pas. Veuillez vérifier la commande et réessayer.")
            


@bot.command()
async def pong(ctx):
    await ctx.send("Ping!")
    print('Commande fonctionnelle !')


@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")


@bot.command()
async def Sinfos(ctx):
    server = ctx.guild
    serveurName = server.name
    numberOfTextChannels = len(server.text_channels)
    numberOfVoiceChannels = len(server.voice_channels)
    numberOfMembers = server.member_count
    owner = server.owner
    serveurRoles = server.roles
    embed = discord.Embed(title = "Serveur Informations", description= "Informations du serveur !", color=0xFFBF66)
    embed.add_field(name = "*Nom du serveur*", value = serveurName, inline=True)
    embed.add_field(name = "*Propriétaire*", value = owner, inline=True)
    embed.add_field(name = "*Membres*", value = numberOfMembers, inline=False)
    embed.add_field(name = "*Salons textuels*", value = numberOfTextChannels, inline=True)
    embed.add_field(name = "*Salons vocaux*", value = numberOfVoiceChannels, inline=True)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1269063423535222858/1269168943898296432/photo-by-patrick-on-unsplash-1649426391.jpg?ex=66af1530&is=66adc3b0&hm=3dfbddd2c6ce8db0c90e8ed88bcd90cef55b146eedaa936be86637e578cb6500&")
    await ctx.send(embed = embed)


@bot.command()
async def say(ctx, *texte):
    await ctx.send(" ".join(texte))

welcome_channel = 1269309406391042145

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(welcome_channel)
    if channel is not None:
        new_member = f"Bienvenue à {member.mention} sur le serveur, nous te souhaitons tous une bonne aventure sur les mers !"
        embed = discord.Embed(
            title="Nouvel arrivant !",
            description=new_member,
            color=0xFFBF66,
            timestamp=datetime.datetime.utcnow()
        )
        
        embed.set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
        embed.set_image(url="https://media1.tenor.com/m/o0NOobSt-AwAAAAC/luffy-gear-5.gif")
        embed.set_footer(text="Nous sommes ravis de vous accueillir !")

        await channel.send(embed=embed)


@bot.command()
@commands.has_permissions(manage_messages=True)  # Assurez-vous que l'utilisateur a la permission de gérer les messages
    
async def clear(ctx, amount: int):
    """Supprime un nombre spécifié de messages du canal actuel, en ignorant les messages du bot."""
    embed_error = discord.Embed(title="Commande invalide", color=0xFFBF66, description="Le nombre de messages à supprimer doit être supérieur à 0.")
    if amount <= 0:
        await ctx.send(embed = embed_error)
        return

    def is_not_bot(message):
        return not message.author.bot

    # Récupérer les messages à supprimer, en excluant ceux du bot
    
    await ctx.channel.purge(limit=amount+1, check=is_not_bot)
    deleted_message = f"{amount} messages supprimés."
    embed_clear = discord.Embed(title="Clear Messages", color=0xFFBF66, description=deleted_message)

    await ctx.send(embed = embed_clear, delete_after=5)
    
@clear.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        embed = discord.Embed(title="Erreur dans la commande", color=0xFFBF66, description="Vous n'avez pas la permission de gérer les messages.")
        await ctx.send(embed = embed)

zoan_classique = {
    "Inu Inu no Mi modèle Loup": {
        "description": "Permet à son utilisateur de devenir entièrement ou partiellement un loup.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Hito Hito no Mi": {
        "description": "Permet à son utilisateur (si animal) de devenir entièrement ou partiellement humain. Si un homme le mange il sera apparemment “éclairé.”",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Mogu Mogu no Mi": {
        "description": "Permet à son utilisateur de devenir entièrement ou partiellement une taupe.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Uma Uma no Mi": {
        "description": "Permet à son utilisateur de devenir entièrement ou partiellement un cheval.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Uma Uma no Mi modèle Zèbre": {
        "description": "Permet à son utilisateur de devenir entièrement ou partiellement un zèbre.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Zo Zo no Mi": {
        "description": "Permet à son utilisateur de devenir entièrement ou partiellement un éléphant.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Kawa Kawa no Mi": {
        "description": "Permet à son utilisateur de devenir entièrement ou partiellement une loutre de mer.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Sara Sara no Mi": {
        "description": "Permet à son utilisateur de devenir entièrement ou partiellement un axolotl.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Koara Koara no Mi": {
        "description": "Permet à son utilisateur de devenir entièrement ou partiellement un koala.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Kame Kame no Mi": {
        "description": "Permet à son utilisateur de devenir entièrement ou partiellement une tortue terrestre.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Neko Neko no Mi modèle Tigre": {
        "description": "Permet à son utilisateur de devenir entièrement ou partiellement un tigre.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Neko Neko no Mi modèle Guépard": {
        "description": "Permet à son utilisateur de devenir entièrement ou partiellement un guépard.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Rama Rama no Mi": {
        "description": "Permet à son utilisateur de devenir entièrement ou partiellement un lama.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Rama Rama no Mi": {
        "description": "Permet à son utilisateur de devenir entièrement ou partiellement un lama.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Ushi Ushi no mi modèle Bison": {
        "description": "Permet à son utilisateur de devenir entièrement ou partiellement un bison.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Ushi Ushi no mi modèle Girafe": {
        "description": "Permet à son utilisateur de devenir entièrement ou partiellement une girafe.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Ushi Ushi no mi modèle Rhinocéros": {
        "description": "Permet à son utilisateur de devenir entièrement ou partiellement un Rhinocéros.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Ushi Ushi no mi modèle taureau (minotaure)": {
        "description": "Permet à son utilisateur de devenir entièrement ou partiellement un taureau.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Inu Inu no mi modèle Basset": {
        "description": "Permet à son utilisateur de devenir entièrement ou partiellement un canidé, plus précisément un Basset.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Inu Inu no mi modèle Chacal": {
        "description": "Permet à son utilisateur de devenir entièrement ou partiellement un canidé, plus précisément un chacal.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Inu Inu no mi modèle Loup": {
        "description": "Permet à son utilisateur de devenir entièrement ou partiellement un loup.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Inu Inu no mi modèle Dalmatien": {
        "description": "Permet à son utilisateur de devenir entièrement ou partiellement un chien de la race dalmatien.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Inu Inu no mi modèle Chihuahua": {
        "description": "Permet à son utilisateur de devenir entièrement ou partiellement un chien de la race Chihuahua.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Inu Inu no mi modèle Tanuki": {
        "description": "Permet à son utilisateur de devenir entièrement ou partiellement un tanuki.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Tori Tori no mi modèle Aigle": {
        "description": "Permet à son utilisateur de devenir entièrement ou partiellement un aigle.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Tori Tori no mi modèle Faucon": {
        "description": "Permet à son utilisateur de devenir entièrement ou partiellement un faucon.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Tori Tori no mi modèle Albatros": {
        "description": "Permet à son utilisateur de devenir entièrement ou partiellement un albatros.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Tama Tama no mi": {
        "description": "Permet à son utilisateur de devenir entièrement ou partiellement un œuf.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Hebi Hebi no mi modèle Anaconda": {
        "description": "Permet à son utilisateur de devenir entièrement ou partiellement un anaconda.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Hebi Hebi no mi modèle Cobra royal": {
        "description": "Permet à son utilisateur de devenir entièrement ou partiellement un cobra royal.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Kumo Kumo no mi (Onigumo)": {
        "description": "Permet à son utilisateur de devenir entièrement ou partiellement un cobra araignée.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Mushi Mushi no mi modèle Scarabée Rhinocéros": {
        "description": "Permet à son utilisateur de devenir entièrement ou partiellement un scarabée rhinocéros.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Mushi Mushi no mi modèle Abeille": {
        "description": "Permet à son utilisateur de devenir entièrement ou partiellement une abeille.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Mushi Mushi no mi modèle Chenille": {
        "description": "Permet à son utilisateur de devenir entièrement ou partiellement une chenille.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    }

    
}

zoan_antique = {
    "Neko Neko no mi modèle Tigre à dents de sabre": {
        "description": "Permet à son utilisateur de devenir entièrement ou partiellement un Tigre à dents de sabre.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Kumo Kumo no mi modèle Rosa Mygale Grauvogeli": {
        "description": "Permet à son utilisateur de devenir entièrement ou partiellement une Rosa mygale Grauvogeli.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Zo Zo no mi modèle Mammouth": {
        "description": "Permet à son utilisateur de devenir entièrement ou partiellement un mammouth.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Ryu Ryu no mi modèle Allosaure": {
        "description": "Permet à son utilisateur de devenir entièrement ou partiellement un Allosaure.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Ryu Ryu no mi modèle Spinosaure": {
        "description": "Permet à son utilisateur de devenir entièrement ou partiellement un Spinosaure.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Ryu Ryu no mi modèle Ptéranodon": {
        "description": "Permet à son utilisateur de devenir entièrement ou partiellement un Ptéranodon.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Ryu Ryu no mi modèle Prachéchyosaure": {
        "description": "Permet à son utilisateur de devenir entièrement ou partiellement un Pachycéphalosaure.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Ryu Ryu no mi modèle Tricératops": {
        "description": "Permet à son utilisateur de devenir entièrement ou partiellement un Tricératops.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Ryu Ryu no mi modèle Brachiosaure": {
        "description": "Permet à son utilisateur de devenir entièrement ou partiellement un Brachiosaure.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    }
}

logia = {
     "Moku Moku no mi": {
        "description": "Permet à l'utilisateur de créer, contrôler et se transformer en fumée.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Mera Mera no mi": {
        "description": "Permet à l'utilisateur de créer, contrôler et se transformer en flammes.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Magu Magu no mi": {
        "description": "Permet à l'utilisateur de créer, contrôler et se transformer en magma.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Suna Suna no mi": {
        "description": "Permet à l'utilisateur de créer, contrôler et se transformer en sable.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Goro Goro no mi": {
        "description": "Permet à l'utilisateur de créer, contrôler et se transformer en électricité.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Hie Hie no mi": {
        "description": "Permet à l'utilisateur de créer, contrôler et se transformer en glace.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Yuki Yuki no mi": {
        "description": "Permet à l'utilisateur de créer, contrôler et se transformer en neige.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Mori Mori no mi": {
        "description": "Permet à l'utilisateur de créer, contrôler et se transformer en végétaux.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Susu Susu no mi": {
        "description": "Permet à l'utilisateur de créer, contrôler et se transformer en suie.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Numa Numa no mi": {
        "description": "Permet à l'utilisateur de créer, contrôler et se transformer en marais.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Toro Toro no mi": {
        "description": "Permet à l'utilisateur de créer, contrôler et se transformer en liquide.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Pasa Pasa no mi": {
        "description": "Permet à l'utilisateur de créer, contrôler et se transformer en papier ainsi que contrôler ce qui est inscrit dessus.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Ame Ame no mi": {
        "description": "Permet à l'utilisateur de créer, contrôler et se transformer en sirop visqueux.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Pika Pika no mi": {
        "description": "Permet à l'utilisateur de créer, contrôler et se transformer en lumière.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    }
}

zoan_mythique = {
   "Hito Hito no mi modèle Onyudu": {
        "description": "Permet à son utilisateur de devenir entièrement ou partiellement un moine onyudu.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Hito Hito no mi modèle Daibutsu": {
        "description": "Permet à son utilisateur de devenir entièrement ou partiellement un géant Daibutsu, statue d’or de bouddha.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Hebi Hebi no mi modèle Yamata no Orochi": {
        "description": "Permet à son utilisateur de devenir entièrement ou partiellement une hydre à 8 têtes.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Uo Uo no mi modèle Seiryu": {
        "description": "Permet à son utilisateur de devenir entièrement ou partiellement un dragon azur.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Inu Inu no mi modèle Okuchi no Makami": {
        "description": "Permet à son utilisateur de devenir entièrement ou partiellement un loup divin.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Inu Inu no mi modèle Kyubi no Kitsune": {
        "description": "Permet à son utilisateur de devenir entièrement ou partiellement un Kyubi, renard à 9 queues.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Uma Uma no mi modèle Pégase": {
        "description": "Permet à son utilisateur de devenir entièrement ou partiellement un pégase.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Tori Tori no mi modèle Phénix": {
        "description": "Permet à son utilisateur de devenir entièrement ou partiellement un phénix ardent.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Tori Tori no mi modèle Nue": {
        "description": "Permet à son utilisateur de devenir entièrement ou partiellement une nue mythologique, espèce de créature volante et enflammée à tête de singe, corps de lion et griffes de tigre.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Bato Bato no mi modèle Vampire": {
        "description": "Permet à son utilisateur de devenir entièrement ou partiellement un vampire, homme chauve-souris mythologique.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    }
}

paramecias_corporel = {
    "Gomu Gomu no mi": {
        "description": "Permet à l'utilisateur de devenir aussi élastique que du caoutchouc.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Bara Bara no mi": {
        "description": "Permet à l'utilisateur de fragmenter son corps, le rendant insensible à toute lame.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Beri Beri no mi": {
        "description": "Permet à l'utilisateur de fragmenter son corps en boules de différentes tailles, le rendant insensible aux attaques à mains nues.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Sube Sube no mi": {
        "description": "Permet à l'utilisateur d’avoir le corps plus glissant que du beurre fondu.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Kilo Kilo no mi": {
        "description": "Permet à l'utilisateur de changer son poids de 1kg jusqu'à 10 000 kg.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Ton Ton no mi": {
        "description": "Permet à l'utilisateur de faire varier son poids (semble avoir moins de limite que le kilo).",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Bomu Bomu no mi": {
        "description": "Permet à l'utilisateur de créer une explosion à partir de n’importe quelle partie de son corps.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Baku Baku no mi": {
        "description": "Permet à l'utilisateur de manger toute matière sans problème digestif pour en acquérir les propriétés.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Mane Mane no mi": {
        "description": "Permet à l'utilisateur de copier le visage de n’importe qui après l’avoir touché.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Supa Supa no mi": {
        "description": "Permet à l'utilisateur de transformer n’importe quelle partie de son corps en sabre tranchant.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Toge Toge no mi": {
        "description": "Permet à l'utilisateur de créer comme des piques d’oursin sur n’importe quelle partie de son corps.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Bane Bane no mi": {
        "description": "Permet à l'utilisateur de transformer n’importe quelle partie de son corps en ressort.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Shari Shari no mi": {
        "description": "Permet à l'utilisateur de faire tourner n’importe quelle partie de son corps comme une roue.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Suke Suke no mi": {
        "description": "Permet à l'utilisateur de devenir invisible.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Shiro Shiro no mi": {
        "description": "Permet à l'utilisateur de devenir une forteresse vivante pouvant transporter des personnes et objets miniaturisés.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Fruit d’Urouge": {
        "description": "Permet à l'utilisateur de convertir les dégâts reçus en taille et en puissance brute.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Choki Choki no mi": {
        "description": "Permet à l'utilisateur de transformer son corps en ciseaux d’un tranchant extrême.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Kira Kira no mi": {
        "description": "Permet à l'utilisateur de transformer son corps en diamant, le rendant d’une immense résistance.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Poke Poke no mi": {
        "description": "Permet à l'utilisateur d’avoir des poches sur son corps pour ranger sans limite des objets de grande taille.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Deka Deka no mi": {
        "description": "Permet à l'utilisateur d'augmenter sa taille considérablement.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Buki Buki no mi": {
        "description": "Permet à l'utilisateur de transformer son corps en toutes sortes d’armes.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Guru Guru no mi": {
        "description": "Permet à l'utilisateur de changer des parties de son corps en hélices pour s’envoler.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Jake Jake no mi": {
        "description": "Permet à l'utilisateur de devenir une veste pouvant être enfilé par un autre individu.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Pamu Pamu no mi": {
        "description": "Permet à l'utilisateur de faire éclater des parties de son corps pour produire des explosions.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Kibi Kibi no mi": {
        "description": "Permet à l'utilisateur de créer à partir de son corps des mochi pouvant aider à apprivoiser des créatures sauvages.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Netsu Netsu no mi": {
        "description": "Permet à l'utilisateur de chauffer à une température extrême son corps peuvent même s'enflammer.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Riki Riki no mi": {
        "description": "Permet à l'utilisateur d'augmenter à un niveau extrême sa force.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Nomi Nomi no mi": {
        "description": "Permet à l'utilisateur d’avoir une mémoire sans limite.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Kama Kama no mi": {
        "description": "Permet à l'utilisateur de créer des lames d’airs à partir de ces ongles devenus longs et tranchants.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Kachi Kachi no mi": {
        "description": "Permet à l'utilisateur d’augmenter la température et la résistance de son corps.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Atsu Atsu no mi": {
        "description": "Permet à l'utilisateur de faire émaner de son corps de la chaleur jusqu'à 10 000 degrés.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Bana Bana no mi": {
        "description": "Permet à l'utilisateur de convertir son sentiment de jalousie en chaleur, au point de pouvoir s'enflammer.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Gutsu Gutsu no mi": {
        "description": "Permet à l'utilisateur de pouvoir faire fondre le métal pour le forger sans outil ni support.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Mini Mini no mi": {
        "description": "Permet à l'utilisateur de rétrécir jusqu’à 5 millimètres.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Ami Ami no mi": {
        "description": "Permet à l'utilisateur de créer et devenir des filets.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Nito Nito no mi": {
        "description": "Permet à l'utilisateur de produire de la nitroglycérine par sa transpiration, pouvant faire exploser ce dernier.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Koro Koro no mi": {
        "description": "Permet à l'utilisateur de devenir entièrement ou partiellement un wagon.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Nibi Nibi no mi": {
        "description": "Permet à l'utilisateur de reproduire l'apparence d’une personne décédée (ne copie pas les capacités).",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Gero Gero no mi": {
        "description": "Permet à l'utilisateur de produire en permanence une odeur répugnante.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    }
}

paramecias_productif = {
    "Hana Hana no mi": {
        "description": "Permet à l'utilisateur de générer des membres de son corps sur n’importe quelle surface autour.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Doru Doru no mi": {
        "description": "Permet à l'utilisateur de générer et manipuler de la cire.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Ori Ori no mi": {
        "description": "Permet à l'utilisateur de créer des anneaux et des barreaux d’acier.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Ito Ito no mi": {
        "description": "Permet à l'utilisateur de créer et contrôler des fils fins.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Awa Awa no mi": {
        "description": "Permet à l'utilisateur de créer et manipuler des bulles de savon.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Doku Doku no mi": {
        "description": "Permet à l'utilisateur de créer et manipuler toutes sortes de poisons en plus d’y être insensible.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Fuku Fuku no mi": {
        "description": "Permet à l'utilisateur de créer des vêtements en tout genre.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Beta Beta no mi": {
        "description": "Permet à l'utilisateur de générer et manipuler du mucus.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Pero Pero no mi": {
        "description": "Permet à l'utilisateur de générer et manipuler des bonbons et de la gélatine.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Bisu Bisu no mi": {
        "description": "Permet à l'utilisateur de créer et manipuler des biscuits en frappant des mains.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Kuri Kuri no mi": {
        "description": "Permet à l'utilisateur de créer et manipuler de la crème brûlée.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Bata Bata no mi": {
        "description": "Permet à l'utilisateur de créer et contrôler du beurre doux.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Bari Bari no mi": {
        "description": "Permet à l'utilisateur de créer des barrières incassables en croisant des doigts.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Goe Goe no mi": {
        "description": "Permet à l'utilisateur de produire des faisceaux sonores similaires à des rayons d’énergie.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Noko Noko no mi": {
        "description": "Permet à l'utilisateur de produire des spores toxiques de champignons.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Jara Jara no mi": {
        "description": "Permet à l'utilisateur de produire des chaînes d’acier à partir de son corps.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Nepa Nepa no mi": {
        "description": "Permet à l'utilisateur de produire des vagues de chaleur et de flammes.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Mono Mono no mi": {
        "description": "Permet à l'utilisateur de créer des clones de lui-même, de quelqu’un d’autre ou d’un objet.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Bai Bai no mi": {
        "description": "Permet à l'utilisateur de créer des répliques de n’importe quel objet non organique.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Mochi Mochi no mi": {
        "description": "Permet à l'utilisateur de créer, contrôler et se transformer en riz gluant.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Meta Meta no mi": {
        "description": "Permet à l'utilisateur de créer, contrôler et se transformer en métal liquide.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    }
}

paramecias_manipulateur = {
    "Noro Noro no Mi": {
        "description": "Permet à l'utilisateur de tirer un rayon qui ralenti les cibles de 30 fois pendant 30 secondes.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Doa Doa no Mi": {
        "description": "Permet à l'utilisateur de créer des portes n’importe où pour se déplacer vers une autre dimension.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Sabi Sabi no Mi": {
        "description": "Permet à l'utilisateur de faire rouiller tout le fer qu’il touche.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Yomi Yomi no Mi": {
        "description": "Permet à l'utilisateur de devenir immortel et de contrôler son esprit hors de son corps.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Kage Kage no Mi": {
        "description": "Permet à l'utilisateur de prendre, manipuler les ombres ainsi que d’en changer les propriétaires.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Horo Horo no Mi": {
        "description": "Permet à l'utilisateur de générer des fantômes déprimants en plus de pouvoir acquérir une forme spectrale hors de son corps.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Jiki Jiki no Mi": {
        "description": "Permet à l'utilisateur de contrôler l'électromagnétisme pour ainsi manipuler le fer autour.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Gura Gura no Mi": {
        "description": "Permet à l'utilisateur de créer des ondes sismiques dévastatrices sur terre comme au ciel, et même en mer.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Woshu Woshu no Mi": {
        "description": "Permet à l'utilisateur d’agir sur les personnes et objets l’entourant comme du linge à laver et étendre.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Fuwa Fuwa no Mi": {
        "description": "Permet à l'utilisateur de faire voler tout objet non vivant à condition de l’avoir touché au préalable.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Mato Mato no Mi": {
        "description": "Permet à l'utilisateur de ne jamais rater sa cible lorsqu’il lance un objet.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Zushi Zushi no Mi": {
        "description": "Permet à l'utilisateur de manipuler la gravité.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Nui Nui no Mi": {
        "description": "Permet à l'utilisateur de coudre ses adversaires et son environnement.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Giro Giro no Mi": {
        "description": "Permet à l'utilisateur de voir à travers toute matière ainsi que de sonder l’esprit des gens.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Ato Ato no Mi": {
        "description": "Permet à l'utilisateur de transformer ce qui l'entoure en œuvre d’art grâce à des nuages artistiques.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Sui Sui no Mi": {
        "description": "Permet à l'utilisateur de nager sur toute surface hors de l’eau.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Hira Hira no Mi": {
        "description": "Permet à l'utilisateur de rendre toute chose rigide aussi flexible qu’un drapeau.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Ishi Ishi no Mi": {
        "description": "Permet à l'utilisateur de manipuler la roche de son environnement.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Fude Fude no Mi": {
        "description": "Permet à l'utilisateur de donner vie à ses dessins.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Nagi Nagi no Mi": {
        "description": "Permet à l'utilisateur d’annuler tous bruits qu’il produit ou qui sont produits dans une zone établie, ou bien d'isoler le son intérieur de sa zone avec celui extérieur.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Chiyu Chiyu no Mi": {
        "description": "Permet à l'utilisateur de soigner rapidement toutes blessures.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Maki Maki no Mi": {
        "description": "Permet à l'utilisateur de créer et contrôler des parchemins de différentes tailles pour y stocker des objets.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Soru Soru no Mi": {
        "description": "Permet à l'utilisateur de prendre l'espérance de vie d’un individu pour augmenter la sienne, ou bien donner vie à des objets non organiques.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Mira Mira no Mi": {
        "description": "Permet à l'utilisateur de créer et contrôler des miroirs ainsi que de les lier à une dimension parallèle.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Buku Buku no Mi": {
        "description": "Permet à l'utilisateur de créer et contrôler des livres pouvant être liés à une dimension parallèle.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Shibo Shibo no Mi": {
        "description": "Permet à l'utilisateur d’essorer n’importe quelle forme de vie afin d’en extraire les liquides vitaux. Il peut également augmenter en taille grâce à ce liquide.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Memo Memo no Mi": {
        "description": "Permet à l'utilisateur d’extraire la mémoire d’un individu sous forme de pellicule cinématographique pour la manipuler.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Hoya Hoya no Mi": {
        "description": "Permet à l'utilisateur de créer et contrôler un génie se battant à ses côtés. Stand power.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Kuku Kuku no Mi": {
        "description": "Permet à l'utilisateur de cuisiner toute matière de son environnement. Mais cela a un goût ignoble.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Gocha Gocha no Mi": {
        "description": "Permet à l'utilisateur de fusionner avec d’autres personnes.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Kobu Kobu no Mi": {
        "description": "Permet à l'utilisateur d’éveiller le potentiel de combat latent des individus autour tout en les reliant au combat.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Oshi Oshi no Mi": {
        "description": "Permet à l'utilisateur de manipuler le sol pour le faire vibrer comme des vagues ou créer des tunnels souterrains.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Juku Juku no Mi": {
        "description": "Permet à l'utilisateur de faire mûrir toute chose, que ce soit augmenter l’âge physique d’un individu ou vieillir son environnement jusqu'à sa putréfaction.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Shiku Shiku no Mi": {
        "description": "Permet à l'utilisateur de contaminer un individu avec toutes sortes de maladies qu’il peut créer, y compris des maladies inconnues comme celle qui change le sexe d’un individu.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Wapu Wapu no Mi": {
        "description": "Permet à l'utilisateur de se téléporter.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Shima Shima no Mi": {
        "description": "Permet à l'utilisateur de fusionner avec une île pour la contrôler.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Gabu Gabu no Mi": {
        "description": "Permet à l'utilisateur de contrôler l’alcool.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Muchi Muchi no Mi": {
        "description": "Permet à l'utilisateur de transformer des objets en fouet ainsi que de soumettre d’autres objets qu’il contrôle comme des esclaves.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Nori Nori no Mi": {
        "description": "Permet à l'utilisateur de chevaucher toutes choses.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Hiso Hiso no Mi": {
        "description": "Permet à l'utilisateur de comprendre les animaux ainsi que de pouvoir parler avec eux.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Mosa Mosa no Mi": {
        "description": "Permet à l'utilisateur de faire pousser rapidement des plantes pour manipuler celles-ci.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Moa Moa no Mi": {
        "description": "Permet à l'utilisateur de renforcer jusqu'à 100 fois la force, la taille et la vitesse de ce qu’il touche.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Kyubu Kyubu no Mi": {
        "description": "Permet à l'utilisateur de fragmenter et transformer ce qu’il touche en cube.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Hore Hore no Mi": {
        "description": "Permet à l'utilisateur de devenir extrêmement charmant, pouvant faire tomber les gens amoureux de lui.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Nuke Nuke no Mi": {
        "description": "Permet à l'utilisateur de passer à travers toute matière non organique.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Iro Iro no Mi": {
        "description": "Permet à l'utilisateur de se peindre rapidement lui-même, quelqu’un d’autre et/ou un objet afin de se camoufler dans son environnement.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Gol Gol no Mi": {
        "description": "Permet à l'utilisateur de contrôler l’or de son environnement.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Ute Ute no Mi": {
        "description": "Permet à l'utilisateur de transformer toute chose non organique qu’il touche en pistolet et canon.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Pocha Pocha no Mi": {
        "description": "Permet à l'utilisateur de faire grossir le corps de quelqu’un.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Deri Deri no Mi": {
        "description": "Permet à l'utilisateur de livrer des objets à n'importe qui dans son champ de vision.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Gemu Gemu no Mi": {
        "description": "Permet à l'utilisateur de créer une dimension qu’il domine semblable à un jeu vidéo qu’il peut modifier.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Chara Chara no Mi": {
        "description": "Permet à l'utilisateur de donner une conscience aux âmes non vivantes ainsi que de fusionner avec d’autres personnes et/ou objets rendus conscients.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Basu Basu no Mi": {
        "description": "Permet à l'utilisateur de transformer tout ce qu’il touche en bombe.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Gasha Gasha no Mi": {
        "description": "Permet à l'utilisateur de manipuler et assembler la matière non organique de son environnement.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    },
    "Kote Kote no Mi": {
        "description": "Permet à l'utilisateur d'invoquer des gantelets géants qu’il peut manipuler à sa guise pour saisir toute chose non vivante.",
        "embed": discord.Embed(title="Fouille effectuée", color=0xFFBF66).set_thumbnail(url="https://png.pngtree.com/png-vector/20230120/ourmid/pngtree-straw-hat-cartoon-illustration-png-image_6562738.png")
    }

}


fdd_list = {
    **paramecias_corporel,
    **paramecias_productif,
    **paramecias_manipulateur,
    **logia,
    **zoan_classique,
    **zoan_antique,
    **zoan_mythique
}

STAFF_ROLES_IDS = [1269838005234044958, 1269837965446610985]  # Modo et Admin


@bot.group(name="fdd", invoke_without_command=True)
async def fdd(ctx):
    """Groupe de commandes pour les fruits du démon."""
    await ctx.send("Utilisez `?fdd liste`, `?fdd inventaire`, ou `?fdd add/remove` pour accéder aux commandes des fruits du démon.")

@fdd.command(name="inventaire")
async def fdd_inventaire(ctx, member: discord.Member = None):
    """Affiche l'inventaire des fruits du démon d'un utilisateur avec l'état 'mangé' si applicable."""
    member = member or ctx.author

    async with aiosqlite.connect('inventory.db') as db:
        # Requête pour récupérer les fruits possédés par l'utilisateur et leur état (mangé ou non)
        query = """
            SELECT fdd_name, eaten
            FROM fdd_inventory
            WHERE user_id = ?
        """
        cursor = await db.execute(query, (member.id,))
        rows = await cursor.fetchall()

    # Log pour vérifier les fruits récupérés
    logging.info(f"Fetched rows for user {member.id}: {rows}")

    if not rows:
        await ctx.send(f"{member.mention} ne possède aucun fruit du démon.")
        return

    # Créer un dictionnaire pour trier les fruits par sous-catégorie
    sorted_fruits = {
        "Paramecia Corporel": [],
        "Paramecia Productif": [],
        "Paramecia Manipulateur": [],
        "Logia": [],
        "Zoan Classique": [],
        "Zoan Antique": [],
        "Zoan Mythique": [],
    }

    # Trier les fruits par sous-catégorie et ajouter "(mangé)" si le fruit est mangé
    for fruit_name, eaten in rows:
        fruit_status = " (mangé)" if eaten == "True" else ""
        # Vérifier si le fruit existe dans fdd_list
        if fruit_name in fdd_list:
            fruit = fdd_list[fruit_name]
            # Récupérer la catégorie du fruit
            if fruit_name in paramecias_corporel:
                sorted_fruits["Paramecia Corporel"].append(f"{fruit_name}{fruit_status}")
            elif fruit_name in paramecias_productif:
                sorted_fruits["Paramecia Productif"].append(f"{fruit_name}{fruit_status}")
            elif fruit_name in paramecias_manipulateur:
                sorted_fruits["Paramecia Manipulateur"].append(f"{fruit_name}{fruit_status}")
            elif fruit_name in logia:
                sorted_fruits["Logia"].append(f"{fruit_name}{fruit_status}")
            elif fruit_name in zoan_classique:
                sorted_fruits["Zoan Classique"].append(f"{fruit_name}{fruit_status}")
            elif fruit_name in zoan_antique:
                sorted_fruits["Zoan Antique"].append(f"{fruit_name}{fruit_status}")
            elif fruit_name in zoan_mythique:
                sorted_fruits["Zoan Mythique"].append(f"{fruit_name}{fruit_status}")
        else:
            # Si le fruit n'est pas trouvé, on l'ajoute dans une catégorie inconnue
            if "Inconnue" not in sorted_fruits:
                sorted_fruits["Inconnue"] = []
            sorted_fruits["Inconnue"].append(f"{fruit_name}{fruit_status}")

    logging.info(f"Sorted fruits for user {member.id}: {sorted_fruits}")

    # Création de l'embed d'inventaire
    embed = discord.Embed(
        title=f"Inventaire des Fruits du Démon de {member.display_name}",
        color=0xFFBF66
    )

    has_content = False
    for category, fruits in sorted_fruits.items():
        if fruits:
            has_content = True
            value = "\n".join(f"**{fruit_name}**" for fruit_name in fruits)
            embed.add_field(name=category, value=value, inline=False)

    if not has_content:
        embed.description = "Aucun fruit dans l'inventaire."

    logging.info(f"Embed content: {embed.to_dict()}")
    await ctx.send(embed=embed)

@fdd.command(name="liste")
async def fdd_liste(ctx):
    """Affiche un menu pour choisir une catégorie de fruits du démon."""
    # Options pour le menu déroulant
    options = [
        discord.SelectOption(label="Paramecia Corporel", description="Voir les Paramecia Corporel", emoji="\ud83c\udfcb️"),
        discord.SelectOption(label="Paramecia Productif", description="Voir les Paramecia Productif", emoji="⚙️"),
        discord.SelectOption(label="Paramecia Manipulateur", description="Voir les Paramecia Manipulateur", emoji="🎭"),
        discord.SelectOption(label="Logia", description="Voir les Logia", emoji="🔥"),
        discord.SelectOption(label="Zoan Classique", description="Voir les Zoan Classiques", emoji="🐯"),
        discord.SelectOption(label="Zoan Antique", description="Voir les Zoan Antiques", emoji="🧖"),
        discord.SelectOption(label="Zoan Mythique", description="Voir les Zoan Mythiques", emoji="🐉"),
    ]

    # Création du menu déroulant
    select = Select(placeholder="Choisissez une catégorie de FDD", options=options)

    # Callback du menu déroulant
    async def callback(interaction: discord.Interaction):
        category = interaction.data["values"][0]  # Récupère la catégorie sélectionnée

        async with aiosqlite.connect('inventory.db') as db:
            # Construction de la liste des fruits correspondant à la catégorie
            all_fruits = {
                "Paramecia Corporel": list(paramecias_corporel),
                "Paramecia Productif": list(paramecias_productif),
                "Paramecia Manipulateur": list(paramecias_manipulateur),
                "Logia": list(logia),
                "Zoan Classique": list(zoan_classique),
                "Zoan Antique": list(zoan_antique),
                "Zoan Mythique": list(zoan_mythique),
            }.get(category, [])

            # Construction dynamique de placeholders pour la requête SQL
            placeholders = ', '.join(['?'] * len(all_fruits))
            query = f"SELECT fdd_name, eaten FROM fdd_inventory WHERE fdd_name IN ({placeholders}) AND user_id IS NOT NULL"
            cursor = await db.execute(query, all_fruits)
            rows = await cursor.fetchall()

            # Fruits déjà pris avec indication "mangé" si nécessaire
            fruits_pris = [(f"{row[0]} (mangé)" if row[1] == "True" else row[0]) for row in rows]

            # Fruits disponibles
            fruits_disponibles = [fruit for fruit in all_fruits if fruit not in [row[0] for row in rows]]

            # Préparer les sections pour l'embed
            pris_section = "\n".join(fruits_pris) if fruits_pris else "Aucun fruit pris."
            dispo_section = "\n".join(fruits_disponibles) if fruits_disponibles else "Aucun fruit disponible."

            # Création de l'embed
            embed = discord.Embed(
                title=f"Fruits du Démon - {category}",
                color=0xFFBF66
            )
            embed.add_field(name="Fruits Pris", value=pris_section, inline=False)
            embed.add_field(name="Fruits Disponibles", value=dispo_section, inline=False)

            # Envoi de l'embed
            await interaction.response.send_message(embed=embed)

    # Ajouter le callback au menu
    select.callback = callback

    # Ajouter le menu dans une vue
    view = View()
    view.add_item(select)

    # Envoyer le menu
    await ctx.send("Choisissez une catégorie de Fruits du Démon :", view=view)

@fdd.command(name="add")
async def fdd_add(ctx, fruit_name: str, member: discord.Member):
    """Ajoute un fruit du démon à l'inventaire d'un utilisateur (réservée au staff)."""
    # Vérifier si l'utilisateur a un des rôles de staff (Modo ou Admin)
    if not any(role.id in STAFF_ROLES_IDS for role in ctx.author.roles):
        await ctx.send(f"{ctx.author.mention}, vous n'avez pas la permission d'exécuter cette commande.")
        return

    if fruit_name not in fdd_list:
        await ctx.send(f"Le fruit {fruit_name} n'existe pas dans la base de données.")
        return

    async with aiosqlite.connect('inventory.db') as db:
        # Vérifier si le fruit est déjà possédé
        query_check = """
            SELECT user_id FROM fdd_inventory WHERE fdd_name = ?
        """
        cursor = await db.execute(query_check, (fruit_name,))
        row = await cursor.fetchone()

        if row and row[0]:
            await ctx.send(f"Le fruit {fruit_name} est déjà possédé par quelqu'un.")
            return

        # Ajouter le fruit à l'utilisateur
        query_insert = """
            INSERT OR REPLACE INTO fdd_inventory (fdd_name, user_id) VALUES (?, ?)
        """
        await db.execute(query_insert, (fruit_name, member.id))
        await db.commit()

    await ctx.send(f"{member.mention} a reçu le fruit {fruit_name} !")

@fdd.command(name="remove")
async def fdd_remove(ctx, fruit_name: str, member: discord.Member):
    """Retire un fruit du démon de l'inventaire d'un utilisateur (réservée au staff)."""
    # Vérifier si l'utilisateur a un des rôles de staff (Modo ou Admin)
    if not any(role.id in STAFF_ROLES_IDS for role in ctx.author.roles):
        await ctx.send(f"{ctx.author.mention}, vous n'avez pas la permission d'exécuter cette commande.")
        return

    async with aiosqlite.connect('inventory.db') as db:
        # Vérifier si l'utilisateur possède le fruit
        query_check = """
            SELECT user_id FROM fdd_inventory WHERE fdd_name = ? AND user_id = ?
        """
        cursor = await db.execute(query_check, (fruit_name, member.id))
        row = await cursor.fetchone()

        if not row:
            await ctx.send(f"{member.mention} ne possède pas le fruit {fruit_name}.")
            return

        # Retirer le fruit de l'utilisateur
        query_delete = """
            DELETE FROM fdd_inventory WHERE fdd_name = ? AND user_id = ?
        """
        await db.execute(query_delete, (fruit_name, member.id))
        await db.commit()

    await ctx.send(f"Le fruit {fruit_name} a été retiré de l'inventaire de {member.mention}.")

@fdd.command(name="info")
async def fdd_info(ctx, *, fruit_name: str):
    """Affiche les informations détaillées d'un fruit du démon avec son propriétaire.""" 
    # Vérifier si le fruit existe dans la base de données
    if fruit_name not in fdd_list:
        await ctx.send(f"Le fruit du démon {fruit_name} n'existe pas.")
        return

    # Accéder à la base de données pour récupérer les informations sur le fruit
    async with aiosqlite.connect('inventory.db') as db:
        # Récupérer l'ID de l'utilisateur et le statut "mangé"
        query = """
            SELECT user_id, eaten FROM fdd_inventory WHERE fdd_name = ?
        """
        cursor = await db.execute(query, (fruit_name,))
        row = await cursor.fetchone()

    # Si le fruit n'a pas été trouvé dans l'inventaire
    if row is None:
        await ctx.send(f"Le fruit {fruit_name} n'est pas encore possédé.")
        return

    # Récupérer l'utilisateur possédant le fruit
    owner_id = row[0]
    eaten_status = "Oui" if row[1] == "True" else "Non"

    # Obtenir l'objet utilisateur à partir de l'ID
    owner = await ctx.bot.fetch_user(owner_id)

    # Récupérer la description du fruit depuis `fdd_list`
    fruit_info = fdd_list.get(fruit_name)
    description = fruit_info["description"]

    # Créer l'embed
    embed = discord.Embed(
        title=f"Informations sur le fruit du démon : {fruit_name}",
        description=description,
        color=0xFFBF66
    )

    # Ajouter le statut "Mangé" et le propriétaire à l'embed
    embed.add_field(name="Mangé ?", value=eaten_status, inline=False)
    embed.add_field(name="Propriétaire", value=owner.mention, inline=False)

    # Ajouter l'image du fruit (vignette) si disponible
    embed.set_thumbnail(url=fruit_info["embed"].thumbnail.url)

    # Envoyer l'embed
    await ctx.send(embed=embed)

@fdd.command(name="manger")
async def fdd_manger(ctx, fruit_name: str):
    """Permet à un utilisateur de manger un fruit du démon, s'il n'en a pas déjà mangé un."""
    async with aiosqlite.connect('inventory.db') as db:
        # Vérifier si l'utilisateur a déjà mangé un fruit
        query_check = """
            SELECT fdd_name FROM fdd_inventory
            WHERE user_id = ? AND eaten = 'True'
        """
        cursor = await db.execute(query_check, (ctx.author.id,))
        row = await cursor.fetchone()

        if row:
            # Si l'utilisateur a déjà mangé un fruit, on lui dit qu'il ne peut pas en manger un autre
            await ctx.send(f"{ctx.author.mention}, vous avez déjà mangé un fruit du démon. Vous ne pouvez pas en manger un autre.")
            return

        # Vérifier si le fruit demandé existe et s'il appartient à l'utilisateur
        query_check_fruit = """
            SELECT eaten FROM fdd_inventory WHERE user_id = ? AND fdd_name = ?
        """
        cursor = await db.execute(query_check_fruit, (ctx.author.id, fruit_name))
        row = await cursor.fetchone()

        if not row:
            # Si l'utilisateur ne possède pas ce fruit
            await ctx.send(f"{ctx.author.mention}, vous ne possédez pas le fruit {fruit_name}.")
            return

        if row[0] == "True":
            # Si le fruit est déjà mangé, on l'informe
            await ctx.send(f"{ctx.author.mention}, vous avez déjà mangé le fruit {fruit_name}.")
            return

        # Marquer le fruit comme mangé
        query_update = """
            UPDATE fdd_inventory
            SET eaten = 'True'
            WHERE user_id = ? AND fdd_name = ?
        """
        await db.execute(query_update, (ctx.author.id, fruit_name))
        await db.commit()

        # Message de confirmation
        await ctx.send(f"{ctx.author.mention} a mangé le fruit {fruit_name} ! Vous ne pouvez plus manger d'autres fruits.")

@fdd.command(name="trade")
async def fdd_trade(ctx, fruit_name: str, member: discord.Member):
    """Permet de transférer un fruit du démon à un autre utilisateur si les deux parties acceptent."""
    async with aiosqlite.connect('inventory.db') as db:
        # Vérifier si le fruit appartient à l'utilisateur qui propose l'échange
        query_check = """
            SELECT user_id, eaten FROM fdd_inventory
            WHERE fdd_name = ? AND user_id = ?
        """
        cursor = await db.execute(query_check, (fruit_name, ctx.author.id))
        row = await cursor.fetchone()

        if not row:
            # Si le fruit n'appartient pas à l'utilisateur
            await ctx.send(f"{ctx.author.mention}, vous ne possédez pas le fruit {fruit_name}.")
            return

        if row[1] == "True":
            # Si le fruit a été mangé
            await ctx.send(f"{ctx.author.mention}, vous ne pouvez pas échanger le fruit {fruit_name} car il a déjà été mangé.")
            return

    # Demander confirmation à l'autre utilisateur
    await ctx.send(f"{member.mention}, {ctx.author.mention} souhaite vous donner le fruit **{fruit_name}**. Répondez `oui` pour accepter l'échange.")

    def check(message):
        return (
            message.author == member
            and message.channel == ctx.channel
            and message.content.lower() in ["oui", "non"]
        )

    try:
        # Attendre la réponse de l'utilisateur mentionné
        response = await bot.wait_for("message", check=check, timeout=60.0)
    except asyncio.TimeoutError:
        await ctx.send(f"{member.mention} n'a pas répondu à temps. L'échange est annulé.")
        return

    if response.content.lower() == "non":
        await ctx.send(f"{member.mention} a refusé l'échange.")
        return

    # Effectuer le transfert
    async with aiosqlite.connect('inventory.db') as db:
        query_update = """
            UPDATE fdd_inventory
            SET user_id = ?
            WHERE fdd_name = ? AND user_id = ?
        """
        await db.execute(query_update, (member.id, fruit_name, ctx.author.id))
        await db.commit()

    # Confirmation de l'échange
    await ctx.send(f"L'échange a été effectué avec succès ! {member.mention} possède maintenant le fruit **{fruit_name}**.")

# Dictionnaire de mappage des techniques avec les noms de colonnes de la base de données
technique_column_mapping = {
    "Ittôryû": "ittoryu",
    "Nitôryû": "nitoryu",
    "Santôryû": "santoryu",
    "Mûtôryû": "mutoryu",
    "Style du Renard de Feu": "style_du_renard_de_feu",
    "Danse de l'Épée des Remous": "danse_de_lepee_des_remous",
    "Style de Combat Tireur d'Élite": "style_de_combat_tireur_delite",
    "Balle Explosive": "balle_explosive",
    "Balle Incendiaire": "balle_incendiaire",
    "Balle Fumigène": "balle_fumigene",
    "Balle Dégoutante": "balle_degoutante",
    "Balle Cactus": "balle_cactus",
    "Balle Venimeuse": "balle_venimeuse",
    "Balle Électrique": "balle_electrique",
    "Balle Gelante": "balle_gelante",
    "Green Pop": "green_pop",
    "Karaté": "karate",
    "Taekwondo": "taekwondo",
    "Judo": "judo",
    "Boxe": "boxe",
    "Okama Kenpo": "okama_kenpo",
    "Hassoken": "hassoken",
    "Ryusoken": "ryusoken",
    "Jambe noire": "jambe_noire",
    "Gyojin Karaté (simplifié)": "gyojin_karate_simplifie",
    "Rope Action": "rope_action",
    "Ramen Kenpo": "ramen_kenpo",
    "Gyojin Karaté": "gyojin_karate",
    "Art Martial Tontatta": "art_martial_tontatta",
    "Jao Kun Do": "jao_kun_do",
    "Electro": "electro",
    "Sulong": "sulong",
    "Style Personnel": "style_personnel"
}


# Fonction pour créer un menu déroulant pour les catégories
class SkillCategorySelect(Select):
    def __init__(self, categories):
        options = [discord.SelectOption(label=category) for category in categories]
        super().__init__(placeholder="Choisissez une catégorie", options=options)

    async def callback(self, interaction: discord.Interaction):
        category = self.values[0]
        user_id = interaction.user.id 

        # Vérification si l'utilisateur existe dans la base de données
        async with aiosqlite.connect('inventory.db') as db:
            cursor = await db.execute("SELECT * FROM skills WHERE user_id = ?", (user_id,))
            user_data = await cursor.fetchone()

            if user_data is None:
                # Initialisation de l'utilisateur dans la base de données si nécessaire
                await db.execute("INSERT INTO skills (user_id) VALUES (?)", (user_id,))
                await db.commit()
                await interaction.response.send_message(f"L'utilisateur {interaction.user.name} a été initialisé dans la base de données.", ephemeral=True)

        # Créer l'embed avec les techniques de la catégorie sélectionnée
        embed = discord.Embed(title=f"Techniques de {category}", color=0xFFBF66)
        
        for technique, _ in skills_liste[category].items():
            # Trouver le nom de la colonne correspondant à la technique
            technique_column = technique_column_mapping.get(technique, technique.lower().replace(" ", "_").replace("é", "e"))
            
            async with aiosqlite.connect('inventory.db') as db:
                cursor = await db.execute(f"SELECT {technique_column} FROM skills WHERE user_id = ?", (user_id,))
                palier = await cursor.fetchone()
                
                palier_str = "``Techniques non apprise``"
                if palier and palier[0] > 0:
                    palier_str = ["I", "II", "III", "IV", "V", "X"][palier[0] - 1] if palier[0] <= 6 else "X"
                
                embed.add_field(name=technique, value=f"Palier: {palier_str}", inline=False)

        await interaction.response.send_message(embed=embed)

# Fonction pour afficher les informations de base
@bot.group(invoke_without_command=True)
async def skills(ctx):
    """
    Commande de groupe 'skills' qui sert de parent à toutes les commandes liées aux compétences.
    """
    categories = list(skills_liste.keys())  # Récupère les catégories de techniques
    select = SkillCategorySelect(categories)
    view = View()
    view.add_item(select)

    embed = discord.Embed(title="Sélectionner une catégorie de techniques", description="Choisissez une catégorie pour voir les techniques disponibles.", color=0xFFBF66)
    await ctx.send(embed=embed, view=view)



@skills.command()
async def setup(ctx, mention: str = None, technique: str = None, palier: int = None):
    """
    Définit ou met à jour le palier d'une technique pour un utilisateur.
    Si l'utilisateur n'existe pas dans la base de données, il est initialisé.
    """
    if mention:
        # Extraire l'ID utilisateur de la mention (en enlevant les chevrons et '@')
        user_id = int(mention.strip('<@!>'))
    else:
        # Utiliser l'ID de l'auteur de la commande si aucune mention n'est fournie
        user_id = ctx.author.id

    palier_dict = {1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V', 6: 'X'}

    if palier not in palier_dict:
        await ctx.send("Palier invalide. Les paliers vont de 1 à 6.")
        return

    async with aiosqlite.connect('inventory.db') as db:
        # Vérifier si l'utilisateur existe
        cursor = await db.execute("SELECT * FROM skills WHERE user_id = ?", (user_id,))
        user_data = await cursor.fetchone()

        if user_data is None:
            # Si l'utilisateur n'existe pas dans la base, l'initialiser
            await db.execute("INSERT INTO skills (user_id) VALUES (?)", (user_id,))
            await db.commit()

        # Mettre à jour le palier de la technique
        technique_column = technique.lower().replace(" ", "_").replace("é", "e")  # Gérer les caractères spéciaux
        await db.execute(f"UPDATE skills SET {technique_column} = ? WHERE user_id = ?", (palier, user_id))
        await db.commit()

        await ctx.send(f"Le palier de la technique {technique} de {mention} a été mis à jour à {palier_dict[palier]}.")

@skills.command()
async def reset(ctx, mention: str = None, technique: str = None):
    """
    Réinitialise une technique pour un utilisateur en mettant son palier à 0.
    Si l'utilisateur n'existe pas dans la base de données, il est initialisé.
    """
    if not mention or not technique:
        await ctx.send("Veuillez mentionner un utilisateur et fournir le nom de la technique. Exemple : `?skills reset @utilisateur \"Nom de la Technique\"`")
        return

    try:
        # Extraire l'ID utilisateur de la mention (en enlevant les chevrons et '@')
        user_id = int(mention.strip('<@!>'))
    except ValueError:
        await ctx.send("La mention de l'utilisateur est invalide.")
        return

    # Trouver le nom de la colonne correspondant à la technique
    technique_column = technique_column_mapping.get(technique, technique.lower().replace(" ", "_").replace("é", "e"))

    if technique_column not in technique_column_mapping.values():
        await ctx.send(f"La technique '{technique}' est invalide ou non reconnue.")
        return

    async with aiosqlite.connect('inventory.db') as db:
        # Vérifier si l'utilisateur existe
        cursor = await db.execute("SELECT * FROM skills WHERE user_id = ?", (user_id,))
        user_data = await cursor.fetchone()

        if user_data is None:
            # Si l'utilisateur n'existe pas dans la base, l'initialiser
            await db.execute("INSERT INTO skills (user_id) VALUES (?)", (user_id,))
            await db.commit()

        # Réinitialiser le palier de la technique à 0
        await db.execute(f"UPDATE skills SET {technique_column} = 0 WHERE user_id = ?", (user_id,))
        await db.commit()

        await ctx.send(f"La technique '{technique}' de {mention} a été réinitialisée (Technique non apprise).")


# Dictionnaire des descriptions des techniques
technique_descriptions = {
    "Ittôryû": "Style d'épée à une seule lame.",
    "Nitôryû": "Style de combat avec deux épées.",
    "Santôryû": "Technique de combat à trois épées.",
    "Mûtôryû": "Style de combat sans épée.",
    "Style du Renard de Feu": "Un style basé sur la vitesse et la précision.",
    "Danse de l'Épée des Remous": "Une technique fluide et élégante.",
    "Style de Combat Tireur d'Élite": "Maîtrise des tirs de précision.",
    "Balle Explosive": "Une balle causant une explosion à l'impact.",
    "Balle Incendiaire": "Une balle qui s'enflamme à l'impact.",
    "Balle Fumigène": "Une balle qui libère de la fumée.",
    "Balle Dégoutante": "Une balle qui libère une odeur désagréable.",
    "Balle Cactus": "Une balle hérissée de piquants.",
    "Balle Venimeuse": "Une balle qui libère un poison.",
    "Balle Électrique": "Une balle électrifiée à l'impact.",
    "Balle Gelante": "Une balle qui gèle à l'impact.",
    "Green Pop": "Une technique utilisant des projectiles végétaux.",
    "Karaté": "Un art martial traditionnel.",
    "Taekwondo": "Un art martial focalisé sur les coups de pied.",
    "Judo": "Un art martial basé sur les projections.",
    "Boxe": "Un style de combat axé sur les coups de poing.",
    "Okama Kenpo": "Un style unique et excentrique.",
    "Hassoken": "Une technique rare basée sur des vibrations.",
    "Ryusoken": "Un style inspiré par les dragons.",
    "Jambe noire": "Un style de combat utilisant les jambes.",
    "Gyojin Karaté (simplifié)": "Une version simplifiée du karaté des hommes-poissons.",
    "Rope Action": "Un style basé sur l'utilisation de cordes.",
    "Ramen Kenpo": "Un style excentrique inspiré de la cuisine.",
    "Gyojin Karaté": "Le karaté des hommes-poissons.",
    "Art Martial Tontatta": "Un style d'art martial des Tontatta.",
    "Jao Kun Do": "Un style de combat rapide et flexible.",
    "Electro": "Une technique basée sur l'électricité.",
    "Sulong": "Un état spécial des Mink en pleine lune.",
    "Style Personnel": "Un style unique à son utilisateur."
}

# Fonction mise à jour pour afficher les descriptions
@skills.command()
async def info(ctx):
    """
    Affiche un menu déroulant pour sélectionner une catégorie de techniques.
    Lorsque l'utilisateur sélectionne une catégorie, les descriptions des techniques sont affichées.
    """
    categories = list(skills_liste.keys())
    select = SkillCategoryInfoSelect(categories)
    view = View()
    view.add_item(select)

    embed = discord.Embed(title="Sélectionner une catégorie de techniques", description="Choisissez une catégorie pour voir les descriptions des techniques.", color=0xFFBF66)
    await ctx.send(embed=embed, view=view)

class SkillCategoryInfoSelect(Select):
    def __init__(self, categories):
        options = [discord.SelectOption(label=category) for category in categories]
        super().__init__(placeholder="Choisissez une catégorie", options=options)

    async def callback(self, interaction: discord.Interaction):
        category = self.values[0]

        # Créer l'embed avec les descriptions des techniques
        embed = discord.Embed(title=f"Descriptions des techniques : {category}", color=0xFFBF66)
        
        for technique, _ in skills_liste[category].items():
            description = technique_descriptions.get(technique, "Description non disponible.")
            embed.add_field(name=technique, value=description, inline=False)

        await interaction.response.send_message(embed=embed)

@skills.command()
async def upgrade(ctx, technique_name: str):
    """
    Commande pour améliorer une technique spécifique avec un embed.
    La technique ne peut être améliorée que si elle est au minimum au palier 1.
    """
    user_id = ctx.author.id
    technique_column = technique_column_mapping.get(technique_name)
    
    if not technique_column:
        await ctx.send(f"La technique {technique_name} n'existe pas. Vérifiez le nom et réessayez.", ephemeral=True)
        return

    async with aiosqlite.connect('inventory.db') as db:
        # Récupération des points depuis `user_stats` et du palier actuel depuis `skills`
        cursor = await db.execute("""
            SELECT us.points, us.points_spent, s.{}
            FROM user_stats us
            LEFT JOIN skills s ON us.user_id = s.user_id
            WHERE us.user_id = ?
        """.format(technique_column), (user_id,))
        user_data = await cursor.fetchone()

        if not user_data:
            await ctx.send("Vous n'êtes pas enregistré dans la base de données. Veuillez essayer à nouveau après votre initialisation.", ephemeral=True)
            return

        points, points_spent, current_tier = user_data

        # Vérification si le palier est à 0, ce qui signifie que la technique n'est pas encore débloquée
        if current_tier == 0:
            embed = discord.Embed(title="Erreur d'Amélioration", description=f"Votre compétence {technique_name} est au palier 0 et ne peut pas être améliorée. Veuillez demander à un membre du staff de la configurer à un palier d'initiation (1).", color=0xFF0000)
            await ctx.send(embed=embed)
            return

        # Vérification si la compétence est déjà au niveau maximum
        if current_tier >= 6:
            embed = discord.Embed(title="Amélioration de Technique", description=f"Votre compétence {technique_name} est déjà au niveau maximum (X).", color=0xFFBF66)
            await ctx.send(embed=embed)
            return

        # Calcul du coût pour passer au palier suivant
        tier_cost = [0, 6, 12, 18, 24, 30]
        upgrade_cost = tier_cost[current_tier]

        if points < upgrade_cost:
            embed = discord.Embed(title="Amélioration de Technique", description=f"Vous n'avez pas assez de points pour améliorer {technique_name}.", color=0xFFBF66)
            embed.add_field(name="Points nécessaires", value=upgrade_cost, inline=True)
            embed.add_field(name="Points disponibles", value=points, inline=True)
            await ctx.send(embed=embed)
            return

        # Mise à jour des points et du niveau de compétence
        new_tier = current_tier + 1
        new_points = points - upgrade_cost
        new_points_spent = points_spent + upgrade_cost

        await db.execute(f"UPDATE skills SET {technique_column} = ? WHERE user_id = ?", (new_tier, user_id))
        await db.execute("UPDATE user_stats SET points = ?, points_spent = ? WHERE user_id = ?", (new_points, new_points_spent, user_id))
        await db.commit()

        # Embed de réponse avec succès
        embed = discord.Embed(title="Amélioration de Technique", description=f"Félicitations ! Votre compétence {technique_name} a été améliorée.", color=0xFFBF66)
        embed.add_field(name="Nouveau Palier", value=f"{['I', 'II', 'III', 'IV', 'V', 'X'][new_tier - 1]}", inline=True)
        embed.add_field(name="Points restants", value=new_points, inline=True)
        embed.add_field(name="Vôtre Elo", value=new_points_spent, inline=True)
        await ctx.send(embed=embed)

# Commande @bot.command() pour ?roll D
@bot.command()
async def roll(ctx, *, arg=None):
    if arg == "D":  # Vérifier que l'argument est bien "D"
        chance = random.randint(1, 15)  # Génère un nombre entre 1 et 10
        result = "D" if chance == 1 else "Pas D"  # Si c'est 1, alors c'est un "D"

        # Création de l'embed avec la couleur FFBF66
        embed = discord.Embed(
            title="Résultat du lancer de D",
            description=f"Tu as lancé le dé et tu as obtenu : **{result}**",
            color=0xFFBF66  # Couleur FFBF66
        )

        # Ajouter un GIF (remplacer l'URL par un GIF de One Piece en rapport avec le "D")
        embed.set_image(url="https://media.giphy.com/media/your-gif-url.gif")  # Remplacer par le lien réel du GIF

        # Envoi de l'embed
        await ctx.send(embed=embed)
    else:
        await ctx.send("Commande invalide. Utilise `?roll D` pour lancer le dé.")


fouille_cooldown = datetime.timedelta(hours=24)  # Cooldown de 24 heures
user_last_fouille = {}  # Dictionnaire pour stocker les derniers entraînements des utilisateurs

@bot.command(name="fouille")
async def fouille(ctx):
    """Permet aux utilisateurs de fouiller et de potentiellement obtenir des récompenses."""
    user_id = ctx.author.id
    guild = ctx.guild
    category_id = ctx.channel.category_id

    fiche_role = discord.utils.get(ctx.author.roles, id=1270083788529074220)
    
    if not fiche_role:
        embed = discord.Embed(
            title="Fiche non validée",
            description="Vous ne pouvez pas entraîner car votre fiche n'a pas encore été validée.",
            color=0xFF0000
        )
        await ctx.send(embed=embed)
        return

    current_time = datetime.datetime.now()
    last_fouille_time = user_last_fouille.get(ctx.author.id, datetime.datetime.fromtimestamp(0))

    if current_time - last_fouille_time < fouille_cooldown:
        remaining_time = fouille_cooldown - (current_time - last_fouille_time)
        hours, remainder = divmod(remaining_time.total_seconds(), 3600)
        minutes, _ = divmod(remainder, 60)
        time_left = f"{int(hours)} heures et {int(minutes)} minutes"
        
        embed = discord.Embed(
            title="Temps de cooldown",
            description=f"Vous devez attendre encore **{time_left}** avant de pouvoir entraîner cette capacité à nouveau.",
            color=0xFF0000
        )
        await ctx.send(embed=embed)
        return

    # Répartition des probabilités par défaut
    drops = [
        (20, "Rien"),
        (23, "Berry"),
        (23, "Coffre en bois"),
        (15, "Coffre en argent"),
        (10, "Coffre en or"),
        (6, "Parchemin Antique"),
        (1.5, "Fruit Paramecia/Zoan classique"),
        (1, "Fruit Zoan antique/Logia"),
        (0.5, "Fruit Zoan mythique")
    ]

    # Répartition spécifique pour la catégorie 1272046653116780574
    if category_id == 1272046653116780574:
        drops = [
            (23, "Rien"),
            (20, "Berry"),
            (14, "Coffre en bois"),
            (12, "Coffre en argent"),
            (10, "Coffre en or"),
            (8, "Parchemin Antique"),
            (10, "Dial"),
            (1.5, "Fruit Paramecia/Zoan classique"),
            (1, "Fruit Zoan antique/Logia"),
            (0.5, "Fruit Zoan mythique")
        ]

    # Fonction pour tirer un item au hasard
    def get_random_drop():
        total = sum(weight for weight, _ in drops)
        rand = random.uniform(0, total)
        upto = 0
        for weight, item in drops:
            if upto + weight >= rand:
                return item
            upto += weight
        return "Rien"

    reward = get_random_drop()

    embed = discord.Embed(color=0xFFBF66)

    # Message descriptif selon la récompense
    reward_message = {
        "Berry": "Tu as trouvé une somme impressionnante de Berry.",
        "Coffre en bois": "Tu as découvert un coffre en bois. Qui sait ce qu'il contient !",
        "Coffre en argent": "Un coffre en argent brillant se trouve dans tes mains.",
        "Coffre en or": "Félicitations, un coffre en or très rare est à toi !",
        "Parchemin Antique": "Un mystérieux parchemin antique a été trouvé.",
        "Dial": "Un Dial unique est maintenant en ta possession.",
        "Fruit Paramecia/Zoan classique": "Un fruit du démon intéressant t'attend.",
        "Fruit Zoan antique/Logia": "Un fruit du démon rare a été trouvé.",
        "Fruit Zoan mythique": "Un fruit mythique t'appartient désormais.",
        "Rien": "Malheureusement, tu n'as rien trouvé cette fois."
    }

    embed.title = f"Récompense trouvée - {reward}"
    embed.description = f"*{reward_message[reward]}*"

    # Ajouter des récompenses spécifiques
    if reward == "Berry":
        amount = random.randint(100000, 500000)
        embed.add_field(name="Récompense", value=f"-  **{amount} Berry 🪙**")
    elif reward == "Coffre en bois":
        berry_amount = random.randint(50000, 300000)
        lingots = ["Lingot de Fer"]
        lingots_count = {lingot: random.randint(3, 6) for lingot in lingots}
        lingots_str = "\n".join([f"-  **{count} {lingot} 💵**" for lingot, count in lingots_count.items()])
        embed.add_field(name="Récompense", value=f"-  **{berry_amount} Berry 🪙**\n{lingots_str}")
    elif reward == "Coffre en argent":
        berry_amount = random.randint(500000, 1000000)
        lingots = ["Lingot de Fer"]
        lingots_count = {lingot: random.randint(5, 8) for lingot in lingots}
        lingots_rare = random.choice(["Lingot de Titane 💷", "Lingot d'Or 💴"])
        lingots_str = "\n".join([f"-  **{count} {lingot} 💵**" for lingot, count in lingots_count.items()])
        embed.add_field(name="Récompense", value=f"-  **{berry_amount} Berry 🪙**\n{lingots_str}\n-  **1 {lingots_rare}**")
    elif reward == "Coffre en or":
        berry_amount = random.randint(1000000, 1500000)
        lingots = ["Lingot de Fer"]
        lingots_count = {lingot: random.randint(9, 12) for lingot in lingots}
        lingots_rare = random.choice(["Lingot de Titane 💷", "Lingot d'Or 💴"])
        gem = random.choice(["Diamant 💎", "Lingot de Granit Marin 💶"])
        lingots_str = "\n".join([f"-  **{count} {lingot} 💵**" for lingot, count in lingots_count.items()])
        embed.add_field(name="Récompense", value=f"-  **{berry_amount} Berry 🪙**\n{lingots_str}\n-  **1 {lingots_rare}**\n-  **1 {gem} **")
    elif reward == "Parchemin Antique":
        embed.add_field(name="Récompense", value="- 📜 **Parchemin Antique**")
    elif reward == "Dial":
        dial_types = [
            "Axe-Dial", "Eisen-Dial", "Breath-Dial", "Jet-Dial", "Heat-Dial", 
            "Flash-Dial", "Flavor-Dial", "Impact-Dial", "Lampe-Dial", 
            "Milky-Dial", "Reject-Dial", "Audio-Dial", "Hydro-Dial", "Thunder-Dial"
        ]
        dial = random.choice(dial_types)
        embed.add_field(name="Récompense", value=f"-  🐚  **Dial : {dial}**")
    elif "Fruit" in reward:
        # Logique pour gérer l'ajout d'un fruit du démon
        async with aiosqlite.connect('inventory.db') as db:
            # Liste des fruits disponibles à ajouter
            if reward == "Fruit Paramecia/Zoan classique":
                fruit_category = paramecias_corporel + paramecias_productif + paramecias_manipulateur + zoan_classique
            elif reward == "Fruit Zoan antique/Logia":
                fruit_category = zoan_antique + logia
            elif reward == "Fruit Zoan mythique":
                fruit_category = zoan_mythique
            else:
                fruit_category = []

            # Chercher les fruits non possédés par l'utilisateur
            query = f"""
                SELECT fdd_name FROM fdd_inventory
                WHERE fdd_name IN ({', '.join(['?'] * len(fruit_category))})
                AND user_id = ?
            """
            cursor = await db.execute(query, (*fruit_category, user_id))
            taken_fruits = [row[0] for row in await cursor.fetchall()]

            # Sélectionner un fruit disponible
            available_fruits = [fruit for fruit in fruit_category if fruit not in taken_fruits]
            
            if available_fruits:
                fruit = random.choice(available_fruits)
                try:
                    await db.execute(""" 
                        INSERT INTO fdd_inventory (user_id, fdd_name)
                        VALUES (?, ?)
                        ON CONFLICT(user_id, fdd_name) DO NOTHING
                    """, (user_id, fruit))
                    await db.commit()
                    embed.add_field(name="Récompense", value=f"- 🍇 **Fruit du Démon : {fruit}**")
                except Exception as e:
                    logging.error(f"Erreur lors de l'ajout du FDD : {e}")
                    embed.add_field(name="Récompense", value="- ❌ Impossible d'ajouter ce fruit.")
            else:
                embed.add_field(name="Récompense", value="- ❌ Aucun fruit disponible cette fois.")
    else:
        embed.add_field(name="Récompense", value="-  Rien trouvé cette fois. ❌")

    # Mise à jour du dernier moment de fouille
    user_last_fouille[ctx.author.id] = current_time

    await ctx.send(embed=embed)

# Commande test
@bot.command()
async def test(ctx):
    await ctx.send("Test réussi")

@bot.command()
async def singe(ctx):
    try:
        # Supprimer le message de la commande
        await ctx.message.delete()
        
        # Envoyer l'image depuis une URL
        image_url = "https://pbs.twimg.com/media/GS8nXGPWwAAA9eR.jpg"
        await ctx.send(image_url)

    except Exception as e:
        print(f"Une erreur est survenue : {e}")

# Charger les variables d'environnement du fichier .env
load_dotenv()

# Récupérer le token Discord
TOKEN = os.getenv("DISCORD_TOKEN")

# Exemple d'utilisation
print("Le token Discord est :", TOKEN)



bot.run(TOKEN)
