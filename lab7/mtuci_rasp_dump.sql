--
-- PostgreSQL database dump
--

-- Dumped from database version 14.5 (Ubuntu 14.5-0ubuntu0.22.04.1)
-- Dumped by pg_dump version 14.5 (Ubuntu 14.5-0ubuntu0.22.04.1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: subject; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.subject (
    id bigint NOT NULL,
    name character varying NOT NULL
);


ALTER TABLE public.subject OWNER TO postgres;

--
-- Name: teacher; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.teacher (
    id bigint NOT NULL,
    full_name character varying NOT NULL,
    chair character varying NOT NULL,
    subject character varying NOT NULL
);


ALTER TABLE public.teacher OWNER TO postgres;

--
-- Name: timetable; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.timetable (
    id bigint NOT NULL,
    subject character varying NOT NULL,
    pair_numb integer NOT NULL,
    cabinet_numb character varying,
    cabinet_location character varying,
    pair_type character varying,
    date date
);


ALTER TABLE public.timetable OWNER TO postgres;

--
-- Data for Name: subject; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.subject (id, name) FROM stdin;
1	Введение в информационные технологии
2	Высшая математика
3	Физика
4	Русский язык
5	Введение в профессию
6	История
7	Английский язык
8	Физическая культура
\.


--
-- Data for Name: teacher; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.teacher (id, full_name, chair, subject) FROM stdin;
1	Андрей Борисов	СиСС	Физика
2	Иван Иванов	ВТ	Введение в информационные технологии
3	Иван Васильевич	НКТ	Введение в профессию
\.


--
-- Data for Name: timetable; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.timetable (id, subject, pair_numb, cabinet_numb, cabinet_location, pair_type, date) FROM stdin;
16	Введение в информационные технологии	1	344	ОП	Лекция	2022-12-20
17	Физика	2	406	ОП	Практика	2022-12-20
18	Русский язык	3	310	ОП	Практика	2022-12-20
19	История	4	406	ОП	Практика	2022-12-20
20	Введение в информационные технологии	1	УЛК-705	А	Лаб.Работа	2022-12-21
21	Введение в информационные технологии	1	344	ОП	Лекция	2022-12-06
22	Физика	2	406	ОП	Практика	2022-12-06
23	Русский язык	3	310	ОП	Практика	2022-12-06
24	История	4	406	ОП	Практика	2022-12-06
25	Введение в информационные технологии	1	УЛК-705	А	Лаб.Работа	2022-12-07
26	Высшая математика	2	514	ОП	Лекция	2022-12-08
27	Русский язык	3	344	ОП	Лекция	2022-12-08
13	Введение в информационные технологии	3	ВЦ-127	ОП	Практика	2022-12-15
10	Английский язык	4	406	ОП	Практика	2022-12-14
2	Физика	2	342	ОП	Лаб.Работа	2022-12-12
3	Высшая математика	3	514	ОП	Лекция	2022-12-12
4	Высшая математика	2	512	ОП	Практика	2022-12-13
9	История	2	432	ОП	Практика	2022-12-14
14	Высшая математика	4	504	ОП	Практика	2022-12-15
7	Физика	5	226	ОП	Лекция	2022-12-13
5	Физика	3	226	ОП	Лекция	2022-12-13
8	Введение в информационные технологии	1	344	ОП	Лекция	2022-12-14
11	Введение в информационные технологии	1	ВЦ-127	ОП	Лаб.Работа	2022-12-15
1	Введение в информационные технологии	1	221	ОП	Лекция	2022-12-12
6	История	4	301	ОП	Лекция	2022-12-13
12	Английский язык	2	504	ОП	Практика	2022-12-15
15	Введение в информационные технологии	3	406	ОП	Практика	2022-12-09
\.


--
-- Name: subject subject_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.subject
    ADD CONSTRAINT subject_pkey PRIMARY KEY (id);


--
-- Name: subject subject_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.subject
    ADD CONSTRAINT subject_uniq UNIQUE (name);


--
-- Name: teacher teacher_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.teacher
    ADD CONSTRAINT teacher_pkey PRIMARY KEY (id);


--
-- Name: timetable timetable_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.timetable
    ADD CONSTRAINT timetable_pkey PRIMARY KEY (id);


--
-- Name: teacher subject_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.teacher
    ADD CONSTRAINT subject_fkey FOREIGN KEY (subject) REFERENCES public.subject(name) NOT VALID;


--
-- Name: timetable subject_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.timetable
    ADD CONSTRAINT subject_fkey FOREIGN KEY (subject) REFERENCES public.subject(name) NOT VALID;


--
-- PostgreSQL database dump complete
--

