-- -----------------------------
-- Crear la base de datos
-- -----------------------------
CREATE DATABASE IF NOT EXISTS ispc;
USE ispc;

-- -----------------------------
-- Tabla Contactos
-- -----------------------------
CREATE TABLE IF NOT EXISTS contactos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    apellido VARCHAR(100) NOT NULL,
    telefono VARCHAR(20),
    email VARCHAR(100)
);

-- -----------------------------
-- Tabla Productos
-- -----------------------------
CREATE TABLE IF NOT EXISTS productos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    descripcion VARCHAR(255),
    precio DECIMAL(10,2) NOT NULL,
    stock INT DEFAULT 0
);

-- -----------------------------
-- Tabla Clientes
-- -----------------------------
CREATE TABLE IF NOT EXISTS clientes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    contacto_id INT NOT NULL,
    fecha_reg DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (contacto_id) REFERENCES contactos(id)
);

-- -----------------------------
-- Tabla Compras
-- -----------------------------
CREATE TABLE IF NOT EXISTS compras (
    id INT AUTO_INCREMENT PRIMARY KEY,
    cliente_id INT NOT NULL,
    producto_id INT NOT NULL,
    cantidad INT NOT NULL,
    total DECIMAL(10,2) NOT NULL,
    fecha DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (cliente_id) REFERENCES clientes(id),
    FOREIGN KEY (producto_id) REFERENCES productos(id)
);

-- -----------------------------
-- Datos de prueba
-- -----------------------------
INSERT INTO contactos (nombre, apellido, telefono, email) VALUES
('Juan', 'Perez', '1234567890', 'juan@example.com'),
('Ana', 'Gomez', '0987654321', 'ana@example.com');

INSERT INTO productos (nombre, descripcion, precio, stock) VALUES
('Laptop', 'Laptop de 15 pulgadas', 1200.00, 10),
('Mouse', 'Mouse inalámbrico', 25.50, 50);

INSERT INTO clientes (contacto_id) VALUES
(1),
(2);

INSERT INTO compras (cliente_id, producto_id, cantidad, total) VALUES
(1, 1, 1, 1200.00),
(2, 2, 2, 51.00);
