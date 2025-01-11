BEGIN TRANSACTION;
CREATE TABLE fdd_inventory (
            user_id INTEGER,
            fdd_name TEXT UNIQUE,
            description TEXT,
            eaten TEXT DEFAULT "False",
            PRIMARY KEY (user_id, fdd_name),
            FOREIGN KEY (user_id) REFERENCES user_stats (user_id)
        );
INSERT INTO "fdd_inventory" VALUES(578171755366055936,'Tori Tori no mi, modèle : Phoenix',NULL,'False');
INSERT INTO "fdd_inventory" VALUES(578171755366055936,'Magu Magu no mi',NULL,'False');
INSERT INTO "fdd_inventory" VALUES(578171755366055936,'Goro Goro no mi',NULL,'False');
CREATE TABLE skills (
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
        );
INSERT INTO "skills" VALUES(578171755366055936,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO "skills" VALUES('<@578171755366055936>',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
CREATE TABLE user_decorations (
            user_id INTEGER PRIMARY KEY,
            thumbnail_url TEXT,
            icon_url TEXT,
            main_url TEXT,
            color TEXT DEFAULT '#FFBF66',
            ost_url TEXT,
            FOREIGN KEY (user_id) REFERENCES user_stats (user_id)
        );
INSERT INTO "user_decorations" VALUES(578171755366055936,NULL,NULL,'https://images6.alphacoders.com/943/thumb-1920-943909.png','#ad3ad5',NULL);
CREATE TABLE user_stats (
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
        );
INSERT INTO "user_stats" VALUES(513634348575096833,5,5,5,5,5,5,0,0,0,0,0,0);
INSERT INTO "user_stats" VALUES(578171755366055936,5,5,5,5,5,5,0,0,0,0,0,0);
INSERT INTO "user_stats" VALUES(1129480863026000024,5,5,5,5,5,5,0,0,0,0,0,0);
DELETE FROM "sqlite_sequence";
COMMIT;
