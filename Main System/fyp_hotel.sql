-- phpMyAdmin SQL Dump
-- version 4.7.4
-- https://www.phpmyadmin.net/
--
-- 主機: 127.0.0.1
-- 產生時間： 2023-07-17 18:17:18
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
('010046', '153 square feet', 'Single Room', 4, 350),
('020043', '200 square feet', 'Twin Room', 4, 400),
('030043', '250 square feet', 'Double Room', 3, 450),
('040043', '270 square feet', 'Triple Room', 3, 470),
('050043', '300 square feet', 'King Room', 5, 550);

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
(0, 1, 1, 1, '010046', 6),
(1, 1, 0, 0, '020043', 7),
(1, 1, 1, 1, '030043', 8),
(1, 1, 0, 0, '040043', 9),
(1, 1, 1, 1, '050043', 10);

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
  MODIFY `booking_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=87;

--
-- 使用資料表 AUTO_INCREMENT `customer_information`
--
ALTER TABLE `customer_information`
  MODIFY `customer_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=96;

--
-- 使用資料表 AUTO_INCREMENT `room_service`
--
ALTER TABLE `room_service`
  MODIFY `service_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

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
