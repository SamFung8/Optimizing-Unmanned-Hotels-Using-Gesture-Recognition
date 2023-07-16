-- phpMyAdmin SQL Dump
-- version 4.7.4
-- https://www.phpmyadmin.net/
--
-- 主機: 127.0.0.1
-- 產生時間： 2023-07-16 18:36:46
-- 伺服器版本: 10.1.30-MariaDB
-- PHP 版本： 5.6.33

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- 資料庫： `fyp_hotel`
--

-- --------------------------------------------------------

--
-- 資料表結構 `booking_record`
--

CREATE TABLE `booking_record` (
  `booking_id` int(11) NOT NULL,
  `customer_id` int(11) NOT NULL,
  `room_id` varchar(11) NOT NULL,
  `check_in_time` datetime NOT NULL,
  `check_out_time` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- 資料表的匯出資料 `booking_record`
--

INSERT INTO `booking_record` (`booking_id`, `customer_id`, `room_id`, `check_in_time`, `check_out_time`) VALUES
(34, 43, '010043', '2023-07-14 23:13:00', '2023-07-21 02:13:00'),
(35, 44, '010043', '2023-07-14 23:13:00', '2023-07-21 02:13:00'),
(36, 45, '010043', '2023-07-15 12:48:00', '2023-07-22 12:48:00'),
(37, 46, '010046', '2023-07-15 19:23:00', '2023-07-22 19:24:00'),
(38, 47, '010046', '2023-07-15 19:27:00', '2023-07-22 19:27:00'),
(39, 48, '010046', '2023-07-15 19:29:00', '2023-07-29 19:29:00'),
(40, 49, '010046', '2023-07-15 19:30:00', '2023-07-29 19:30:00'),
(41, 50, '010046', '2023-07-15 19:33:00', '2023-07-29 19:33:00'),
(42, 51, '010046', '2023-07-15 19:36:00', '2023-07-15 01:36:00'),
(43, 52, '010046', '2023-07-15 19:44:00', '2023-07-15 19:44:00'),
(44, 53, '010046', '2023-07-15 19:40:00', '2023-07-15 19:40:00'),
(45, 54, '010046', '2023-07-15 19:42:00', '2023-07-15 19:42:00'),
(46, 55, '010046', '2023-07-15 19:43:00', '2023-07-15 19:43:00'),
(47, 56, '010046', '2023-07-15 19:45:00', '2023-07-29 19:45:00'),
(48, 57, '010046', '2023-07-15 19:50:00', '2023-07-15 19:50:00'),
(49, 58, '010046', '2023-07-15 19:51:00', '2023-07-29 19:51:00'),
(50, 59, '010046', '2023-07-15 19:54:00', '2023-07-15 19:54:00'),
(51, 60, '010046', '2023-07-15 19:56:00', '2023-07-15 19:56:00'),
(52, 61, '010046', '2023-07-15 20:07:00', '2023-07-15 20:07:00'),
(53, 62, '010046', '2023-07-15 20:10:00', '2023-07-15 20:10:00'),
(54, 63, '010046', '2023-07-15 20:12:00', '2023-07-15 20:12:00'),
(55, 64, '010046', '2023-07-15 20:15:00', '2023-07-15 20:15:00'),
(56, 65, '010046', '2023-07-15 20:16:00', '2023-07-15 20:16:00'),
(57, 66, '010046', '2023-07-15 20:18:00', '2023-07-15 20:18:00'),
(58, 67, '010046', '2023-07-15 20:19:00', '2023-07-15 20:20:00'),
(59, 68, '010043', '2023-07-15 20:31:00', '2023-07-22 20:31:00'),
(60, 69, '010046', '2023-07-15 20:59:00', '2023-07-29 20:59:00'),
(61, 70, '010046', '2023-07-15 21:03:00', '2023-07-29 21:03:00'),
(62, 71, '010046', '2023-07-15 21:30:00', '2023-07-15 21:30:00'),
(63, 72, '010046', '2023-07-15 21:33:00', '2023-07-29 21:33:00'),
(64, 73, '010046', '2023-07-15 21:50:00', '2023-07-29 21:50:00'),
(65, 74, '010046', '2023-07-15 23:22:00', '2023-07-15 23:22:00'),
(66, 75, '010046', '2023-07-15 23:24:00', '2023-07-15 23:24:00'),
(67, 76, '010046', '2023-07-15 23:25:00', '2023-07-15 23:25:00'),
(68, 77, '010046', '2023-07-15 23:32:00', '2023-07-15 23:32:00'),
(69, 78, '010046', '2023-07-15 23:34:00', '2023-07-15 23:34:00'),
(70, 79, '010046', '2023-07-15 23:36:00', '2023-07-15 23:36:00'),
(71, 80, '010046', '2023-07-15 23:39:00', '2023-07-15 23:39:00'),
(72, 81, '010046', '2023-07-15 23:58:00', '2023-07-15 23:58:00'),
(73, 82, '010043', '2023-07-16 15:33:00', '2023-07-29 15:33:00'),
(74, 83, '010043', '2023-07-16 16:24:00', '2023-07-16 16:24:00'),
(75, 84, '010043', '2023-07-16 16:28:00', '2023-07-16 16:28:00'),
(76, 85, '010044', '2023-07-16 23:56:00', '2023-07-23 23:56:00'),
(77, 86, '010043', '2023-07-16 23:57:00', '2023-07-16 23:57:00'),
(78, 87, '010043', '2023-07-16 23:59:00', '2023-07-16 23:59:00'),
(79, 88, '010043', '2023-07-17 00:06:00', '2023-07-17 00:06:00'),
(80, 89, '010043', '2023-07-17 00:10:00', '2023-07-17 00:10:00'),
(81, 90, '010043', '2023-07-17 00:11:00', '2023-07-17 00:11:00'),
(82, 91, '010043', '2023-07-17 00:13:00', '2023-07-17 00:13:00');

-- --------------------------------------------------------

--
-- 資料表結構 `customer_information`
--

CREATE TABLE `customer_information` (
  `customer_id` int(11) NOT NULL,
  `name` varchar(50) NOT NULL,
  `phone_number` int(11) NOT NULL,
  `email` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- 資料表的匯出資料 `customer_information`
--

INSERT INTO `customer_information` (`customer_id`, `name`, `phone_number`, `email`) VALUES
(43, 'Sam', 12345678, NULL),
(44, 'Sam', 12345678, NULL),
(45, 'SAM FUNG', 12345678, NULL),
(46, 'sam', 12345678, NULL),
(47, 'fung', 12345678, NULL),
(48, 'abc', 12, NULL),
(49, 'a', 1, NULL),
(50, 'v', 3, NULL),
(51, 'k', 7, NULL),
(52, 'e', 3, NULL),
(53, 'r', 4, NULL),
(54, 'l', 85454, NULL),
(55, 'q', 2, NULL),
(56, 'e', 2, NULL),
(57, 'f', 2, NULL),
(58, 'q', 3, NULL),
(59, 'g', 4, NULL),
(60, 't', 5, NULL),
(61, 'h', 3, NULL),
(62, 't', 2, NULL),
(63, 'r', 8, NULL),
(64, 'y', 565, NULL),
(65, 'o', 6, NULL),
(66, 't', 5, NULL),
(67, 'fung', 12345678, NULL),
(68, 'FUNG', 23131, NULL),
(69, 'fung', 12345678, NULL),
(70, 'fung', 34342, NULL),
(71, 'sam', 12345678, NULL),
(72, 'same', 12345678, NULL),
(73, 'same', 123214234, NULL),
(74, 'f', 3, NULL),
(75, 'd', 33, NULL),
(76, 'ferfe', 4534, NULL),
(77, 'sam', 1232, NULL),
(78, 'q', 1, NULL),
(79, 'dsds', 34343, NULL),
(80, 'frgr', 3434, NULL),
(81, 'sam', 12345678, NULL),
(82, 'Fung King Shun', 12345678, NULL),
(83, 'Sam', 12345678, 'fungkingsh22@gmail.com'),
(84, 'Sam', 12345678, 'fungkingsh2@gmail.com'),
(85, 'Sam', 12345678, 'fungkingsh2@gmail.com'),
(86, 'Sam', 12345678, 'fungkingsh2@gmail.com'),
(87, 'Sam', 12345678, 'fungkingsh2@gmail.com'),
(88, 'Sam', 12345678, 'fungkingsh2@gmail.com'),
(89, 'Sam', 12345678, 'fungkingsh2@gmail.com'),
(90, 'Sam', 12, 'fungkingsh2@gmail.com'),
(91, 'Sam', 1, 'fungkingsh2@gmail.com');

-- --------------------------------------------------------

--
-- 資料表結構 `room_information`
--

CREATE TABLE `room_information` (
  `room_id` varchar(11) NOT NULL,
  `size` varchar(20) NOT NULL,
  `type` varchar(20) NOT NULL,
  `star_rating` int(11) NOT NULL,
  `price` double NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- 資料表的匯出資料 `room_information`
--

INSERT INTO `room_information` (`room_id`, `size`, `type`, `star_rating`, `price`) VALUES
('010043', '150 square feet', 'Single Room', 3, 300),
('010044', '160 square feet', 'Single Room', 4, 310),
('010046', '153 square feet', 'Single Room', 4, 350);

-- --------------------------------------------------------

--
-- 資料表結構 `room_service`
--

CREATE TABLE `room_service` (
  `wifi` int(11) NOT NULL,
  `breakfast` int(11) NOT NULL,
  `parking` int(11) NOT NULL,
  `spa` int(11) NOT NULL,
  `room_id` varchar(11) NOT NULL,
  `service_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- 資料表的匯出資料 `room_service`
--

INSERT INTO `room_service` (`wifi`, `breakfast`, `parking`, `spa`, `room_id`, `service_id`) VALUES
(1, 0, 0, 0, '010043', 4),
(1, 1, 0, 1, '010044', 5),
(0, 1, 1, 1, '010046', 6);

--
-- 已匯出資料表的索引
--

--
-- 資料表索引 `booking_record`
--
ALTER TABLE `booking_record`
  ADD PRIMARY KEY (`booking_id`),
  ADD KEY `foreign key 2` (`customer_id`),
  ADD KEY `foreign key 1` (`room_id`);

--
-- 資料表索引 `customer_information`
--
ALTER TABLE `customer_information`
  ADD PRIMARY KEY (`customer_id`);

--
-- 資料表索引 `room_information`
--
ALTER TABLE `room_information`
  ADD PRIMARY KEY (`room_id`);

--
-- 資料表索引 `room_service`
--
ALTER TABLE `room_service`
  ADD PRIMARY KEY (`service_id`),
  ADD KEY `foreign key` (`room_id`);

--
-- 在匯出的資料表使用 AUTO_INCREMENT
--

--
-- 使用資料表 AUTO_INCREMENT `booking_record`
--
ALTER TABLE `booking_record`
  MODIFY `booking_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=83;

--
-- 使用資料表 AUTO_INCREMENT `customer_information`
--
ALTER TABLE `customer_information`
  MODIFY `customer_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=92;

--
-- 使用資料表 AUTO_INCREMENT `room_service`
--
ALTER TABLE `room_service`
  MODIFY `service_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- 已匯出資料表的限制(Constraint)
--

--
-- 資料表的 Constraints `booking_record`
--
ALTER TABLE `booking_record`
  ADD CONSTRAINT `foreign key 1` FOREIGN KEY (`room_id`) REFERENCES `room_information` (`room_id`),
  ADD CONSTRAINT `foreign key 2` FOREIGN KEY (`customer_id`) REFERENCES `customer_information` (`customer_id`);

--
-- 資料表的 Constraints `room_service`
--
ALTER TABLE `room_service`
  ADD CONSTRAINT `foreign key` FOREIGN KEY (`room_id`) REFERENCES `room_information` (`room_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
