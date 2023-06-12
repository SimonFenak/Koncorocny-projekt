-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Hostiteľ: 127.0.0.1
-- Čas generovania: Po 12.Jún 2023, 12:52
-- Verzia serveru: 10.4.24-MariaDB
-- Verzia PHP: 8.1.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Databáza: `pythonik`
--

-- --------------------------------------------------------

--
-- Štruktúra tabuľky pre tabuľku `main`
--

CREATE TABLE `main` (
  `meno` varchar(20) NOT NULL,
  `heslo` varchar(100) NOT NULL,
  `raketka` int(10) NOT NULL,
  `bludisko` int(10) NOT NULL,
  `fareb` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Sťahujem dáta pre tabuľku `main`
--

INSERT INTO `main` (`meno`, `heslo`, `raketka`, `bludisko`, `fareb`) VALUES
('jakub', '229990d0b77c8a5748ff018bd474f9d5532b708ea983bb4fcb5a4e91996800ac', 10, 100, 27),
('dominik ', 'aeed2deb1051bd5413226be9b0ab21b797c139b4789101e66dc57cbb62794aae', 0, 100, 50),
('simon', 'aa23a68e9346c329d8a18178be93d4855e21e2cbddd95ebb381a293067fa0cee', 0, 100, 50);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
