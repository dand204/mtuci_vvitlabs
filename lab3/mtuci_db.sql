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
-- Name: chair; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.chair (
    id integer NOT NULL,
    name character varying NOT NULL,
    deanery character varying NOT NULL
);


ALTER TABLE public.chair OWNER TO admin;

--
-- Name: chair_id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

CREATE SEQUENCE public.chair_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.chair_id_seq OWNER TO admin;

--
-- Name: chair_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: admin
--

ALTER SEQUENCE public.chair_id_seq OWNED BY public.chair.id;


--
-- Name: student; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.student (
    id integer NOT NULL,
    full_name character varying NOT NULL,
    passport_data character varying(10) NOT NULL,
    group_numb character varying NOT NULL,
    rating character varying
);


ALTER TABLE public.student OWNER TO admin;

--
-- Name: student_group; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.student_group (
    id integer NOT NULL,
    numb character varying NOT NULL,
    chair_name character varying NOT NULL
);


ALTER TABLE public.student_group OWNER TO postgres;

--
-- Name: student_group_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.student_group_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.student_group_id_seq OWNER TO postgres;

--
-- Name: student_group_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.student_group_id_seq OWNED BY public.student_group.id;


--
-- Name: student_id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

CREATE SEQUENCE public.student_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.student_id_seq OWNER TO admin;

--
-- Name: student_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: admin
--

ALTER SEQUENCE public.student_id_seq OWNED BY public.student.id;


--
-- Name: chair id; Type: DEFAULT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.chair ALTER COLUMN id SET DEFAULT nextval('public.chair_id_seq'::regclass);


--
-- Name: student id; Type: DEFAULT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.student ALTER COLUMN id SET DEFAULT nextval('public.student_id_seq'::regclass);


--
-- Name: student_group id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.student_group ALTER COLUMN id SET DEFAULT nextval('public.student_group_id_seq'::regclass);


--
-- Data for Name: chair; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public.chair (id, name, deanery) FROM stdin;
1	????????	??????????
2	????????	??????????
\.


--
-- Data for Name: student; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public.student (id, full_name, passport_data, group_numb, rating) FROM stdin;
10	???????? ??????????	7483759898	??????2205	824
2	???????? ????????????	4577867888	??????2101	768
11	???????????? ??????????????	9483758542	??????2201	516
9	???????????????? ??????????????	7416759898	??????2205	656
8	???????? ????????????????	7413359898	??????2205	864
15	???????????? ????????????	9996541853	??????2102	976
13	?????????? ????????????????	5138432449	??????2201	670
6	?????????? ??????????????	7123579898	??????2205	615
7	?????????? ??????????????????	7125559898	??????2205	892
1	???????? ????????????	2133567888	??????2101	900
3	???????? ????????????	7899967888	??????2101	899
12	?????????? ??????????????	8769432589	??????2201	694
14	???????????????????? ??????????????????	6794113766	??????2102	817
16	???????????? ????????????	2496883894	??????2102	991
5	?????????? ??????????????	2133578898	??????2101	900
4	?????????? ??????????????	9733564888	??????2101	900
\.


--
-- Data for Name: student_group; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.student_group (id, numb, chair_name) FROM stdin;
1	??????2205	????????
2	??????2101	????????
3	??????2201	????????
4	??????2102	????????
\.


--
-- Name: chair_id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin
--

SELECT pg_catalog.setval('public.chair_id_seq', 2, true);


--
-- Name: student_group_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.student_group_id_seq', 4, true);


--
-- Name: student_id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin
--

SELECT pg_catalog.setval('public.student_id_seq', 16, true);


--
-- Name: chair chair_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.chair
    ADD CONSTRAINT chair_pkey PRIMARY KEY (id);


--
-- Name: chair chair_unic; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.chair
    ADD CONSTRAINT chair_unic UNIQUE (name);


--
-- Name: student_group student_group_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.student_group
    ADD CONSTRAINT student_group_pkey PRIMARY KEY (id);


--
-- Name: student_group student_group_unic; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.student_group
    ADD CONSTRAINT student_group_unic UNIQUE (numb);


--
-- Name: student student_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.student
    ADD CONSTRAINT student_pkey PRIMARY KEY (id);


--
-- Name: student_group chair_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.student_group
    ADD CONSTRAINT chair_fkey FOREIGN KEY (chair_name) REFERENCES public.chair(name) NOT VALID;


--
-- Name: student student_group_fkey; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.student
    ADD CONSTRAINT student_group_fkey FOREIGN KEY (group_numb) REFERENCES public.student_group(numb) NOT VALID;


--
-- PostgreSQL database dump complete
--

