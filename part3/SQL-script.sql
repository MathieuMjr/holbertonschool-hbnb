-- script that create every tables and some initial datas --
CREATE TABLE IF NOT EXISTS `users`(
    `id` CHAR(36) PRIMARY KEY, --UUID !--
    `first_name` VARCHAR(255) NOT NULL,
    `last_name` VARCHAR(255) NOT NULL,
    `email` VARCHAR(255) UNIQUE NOT NULL,
    `password` VARCHAR(255) NOT NULL,
    `is_admin` BOOLEAN NOT NULL DEFAULT 0
);

CREATE TABLE IF NOT EXISTS `places`(
    `id` CHAR(36) PRIMARY KEY, --UUID
    `title` VARCHAR(255) NOT NULL,
    `description` TEXT NOT NULL,
    `price` DECIMAL(10, 2) NOT NULL,
    `latitude` FLOAT NOT NULL,
    `longitude` FLOAT NOT NULL,
    `owner_id` CHAR(36),
    FOREIGN KEY (`owner_id`) REFERENCES `users`(`id`)
);

CREATE TABLE IF NOT EXISTS `amenities`(
    `id` CHAR(36) PRIMARY KEY, --(UUID format)
    `name` VARCHAR(255) UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS `reviews`(
    `id` CHAR(36) PRIMARY KEY, --(UUID format).
    `text` TEXT NOT NULL,
    `rating` INT CHECK(`rating` BETWEEN 1 AND 5),
    `user_id` CHAR(36) NOT NULL,
    `place_id` CHAR(36) NOT NULL,
    FOREIGN KEY (`user_id`) REFERENCES `users`(`id`),
    FOREIGN KEY (`place_id`) REFERENCES `places`(`id`),
    UNIQUE (`place_id`, `user_id`)
);

CREATE TABLE IF NOT EXISTS `place_amenity`(
    `place_id` CHAR(36) NOT NULL,
    `amenity_id` CHAR(36) NOT NULL,
    FOREIGN KEY (`amenity_id`) REFERENCES `amenities`(`id`),
    FOREIGN KEY (`place_id`) REFERENCES `places`(`id`),
    PRIMARY KEY(`place_id`, `amenity_id`)
);

INSERT INTO `users`(
    id, 
    email,
    first_name,
    last_name,
    password,
    is_admin
) VALUES (
    "36c9050e-ddd3-4c3b-9731-9f487208bbc1",
    "admin@hbnb.io",
    "Admin",
    "HBnB",
    "$2a$12$wjXBGB0jtT.ek/W7v3xiGOMA8Qv1fvfUne1ZJuyT3KtainbF2zzua",
    1
);

INSERT INTO amenities(
    id, name
) VALUES ("5331e689-3d34-43c9-be01-a51c22330989", "WiFi" ),
("ed6d39f9-66b8-4ea6-bd30-0d327e585b99", "Swimming Pool"),
("79e2eda2-4f3f-4517-aa34-f57de9fa9946", "Air Conditioning");