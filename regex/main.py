import re

logs = """
2023-12-20 08:40:04 | INFO | 10 | 139681758751632 | decorators.py:78 | send_data_to_fm took 0.093 seconds
2023-12-20 15:40:04	
2023-12-20 08:40:04 | INFO | 10 | 140116180991728 | decorators.py:78 | send_data_to_fm took 0.101 seconds
2023-12-20 15:40:03	
2023-12-20 08:40:03 | INFO | 10 | 140116180991728 | decorators.py:78 | send_data_to_fm took 0.104 seconds
2023-12-20 15:40:02	
2023-12-20 08:40:02 | INFO | 10 | 139681758751632 | decorators.py:78 | send_data_to_fm took 0.192 seconds
2023-12-20 15:40:02	
2023-12-20 08:40:02 | INFO | 10 | 140116180991728 | decorators.py:78 | send_data_to_fm took 0.181 seconds
2023-12-20 15:40:00	
2023-12-20 08:40:00 | INFO | 10 | 140116180991728 | decorators.py:78 | send_data_to_fm took 0.097 seconds
2023-12-20 15:39:55	
2023-12-20 08:39:55 | INFO | 9 | 140116199573840 | decorators.py:78 | send_data_to_fm took 0.099 seconds
2023-12-20 15:39:53	
2023-12-20 08:39:53 | INFO | 9 | 139681706912656 | decorators.py:78 | send_data_to_fm took 0.097 seconds
2023-12-20 15:39:45	
2023-12-20 08:39:45 | INFO | 9 | 139681758739344 | decorators.py:78 | send_data_to_fm took 0.181 seconds
2023-12-20 15:39:41	
2023-12-20 08:39:41 | INFO | 9 | 140116164270992 | decorators.py:78 | send_data_to_fm took 0.099 seconds
2023-12-20 15:39:40	
2023-12-20 08:39:40 | INFO | 10 | 139681758751632 | decorators.py:78 | send_data_to_fm took 0.091 seconds
2023-12-20 15:39:39	
2023-12-20 08:39:39 | INFO | 9 | 140116164270992 | decorators.py:78 | send_data_to_fm took 0.018 seconds
2023-12-20 15:39:24	
2023-12-20 08:39:24 | INFO | 9 | 139681758739344 | decorators.py:78 | send_data_to_fm took 0.098 seconds
2023-12-20 15:39:22	
2023-12-20 08:39:22 | INFO | 9 | 139681758739344 | decorators.py:78 | send_data_to_fm took 0.185 seconds
2023-12-20 15:39:20	
2023-12-20 08:39:20 | INFO | 9 | 140116199573840 | decorators.py:78 | send_data_to_fm took 0.102 seconds
2023-12-20 15:39:02	
2023-12-20 08:39:02 | INFO | 10 | 139681758751344 | decorators.py:78 | send_data_to_fm took 0.096 seconds
2023-12-20 15:38:58	
2023-12-20 08:38:58 | INFO | 10 | 140116199561552 | decorators.py:78 | send_data_to_fm took 0.101 seconds
2023-12-20 15:38:56	
2023-12-20 08:38:56 | INFO | 10 | 139681706883408 | decorators.py:78 | send_data_to_fm took 0.100 seconds
2023-12-20 15:38:38	
2023-12-20 08:38:38 | INFO | 10 | 139681706883408 | decorators.py:78 | send_data_to_fm took 0.105 seconds
2023-12-20 15:38:38	
2023-12-20 08:38:38 | INFO | 10 | 140116199561552 | decorators.py:78 | send_data_to_fm took 0.184 seconds
2023-12-20 15:38:36	
2023-12-20 08:38:36 | INFO | 10 | 139681706883408 | decorators.py:78 | send_data_to_fm took 0.093 seconds
2023-12-20 15:38:36	
2023-12-20 08:38:36 | INFO | 10 | 140116199561552 | decorators.py:78 | send_data_to_fm took 0.106 seconds
2023-12-20 15:38:03	
2023-12-20 08:38:03 | INFO | 9 | 139681706912656 | decorators.py:78 | send_data_to_fm took 0.101 seconds
2023-12-20 15:37:58	
2023-12-20 08:37:58 | INFO | 10 | 140116199561552 | decorators.py:78 | send_data_to_fm took 0.099 seconds
2023-12-20 15:37:54	
2023-12-20 08:37:54 | INFO | 9 | 139681758739632 | decorators.py:78 | send_data_to_fm took 0.101 seconds
2023-12-20 15:37:43	
2023-12-20 08:37:43 | INFO | 10 | 139681706883408 | decorators.py:78 | send_data_to_fm took 0.091 seconds
2023-12-20 15:37:38	
2023-12-20 08:37:38 | INFO | 9 | 140116199573840 | decorators.py:78 | send_data_to_fm took 0.193 seconds
2023-12-20 15:37:05	
2023-12-20 08:37:05 | INFO | 9 | 139681706912656 | decorators.py:78 | send_data_to_fm took 0.101 seconds
2023-12-20 15:36:57	
2023-12-20 08:36:57 | INFO | 9 | 140116199573840 | decorators.py:78 | send_data_to_fm took 0.102 seconds
2023-12-20 15:36:37	
2023-12-20 08:36:37 | INFO | 10 | 139681706883408 | decorators.py:78 | send_data_to_fm took 0.101 seconds
2023-12-20 15:36:29	
2023-12-20 08:36:29 | INFO | 9 | 140116199573840 | decorators.py:78 | send_data_to_fm took 0.109 seconds
2023-12-20 15:36:28	
2023-12-20 08:36:28 | INFO | 9 | 140116199573840 | decorators.py:78 | send_data_to_fm took 0.099 seconds
2023-12-20 15:36:23	
2023-12-20 08:36:23 | INFO | 9 | 140116199573840 | decorators.py:78 | send_data_to_fm took 0.096 seconds
2023-12-20 15:36:22	
2023-12-20 08:36:22 | INFO | 9 | 140116199573840 | decorators.py:78 | send_data_to_fm took 0.101 seconds
2023-12-20 15:36:18	
2023-12-20 08:36:18 | INFO | 10 | 140116199561552 | decorators.py:78 | send_data_to_fm took 0.019 seconds
2023-12-20 15:36:17	
2023-12-20 08:36:17 | INFO | 10 | 140116199561552 | decorators.py:78 | send_data_to_fm took 0.113 seconds
2023-12-20 15:36:17	
2023-12-20 08:36:17 | INFO | 9 | 139681706912656 | decorators.py:78 | send_data_to_fm took 0.106 seconds
2023-12-20 15:36:17	
2023-12-20 08:36:17 | INFO | 10 | 139681706883408 | decorators.py:78 | send_data_to_fm took 0.204 seconds
2023-12-20 15:36:15	
2023-12-20 08:36:15 | INFO | 10 | 140116199561552 | decorators.py:78 | send_data_to_fm took 0.104 seconds
2023-12-20 15:36:08	
2023-12-20 08:36:08 | INFO | 9 | 140116199573840 | decorators.py:78 | send_data_to_fm took 0.099 seconds
2023-12-20 15:36:06	
2023-12-20 08:36:06 | INFO | 10 | 139681706883408 | decorators.py:78 | send_data_to_fm took 0.107 seconds
2023-12-20 15:36:02	
2023-12-20 08:36:02 | INFO | 9 | 139681758739632 | decorators.py:78 | send_data_to_fm took 0.099 seconds
2023-12-20 15:36:02	
2023-12-20 08:36:02 | INFO | 10 | 140116199561552 | decorators.py:78 | send_data_to_fm took 0.183 seconds
2023-12-20 15:35:59	
2023-12-20 08:35:59 | INFO | 10 | 140116199561552 | decorators.py:78 | send_data_to_fm took 0.095 seconds
2023-12-20 15:35:58	
2023-12-20 08:35:58 | INFO | 10 | 140116199561552 | decorators.py:78 | send_data_to_fm took 0.097 seconds
2023-12-20 15:35:57	
2023-12-20 08:35:57 | INFO | 9 | 139681706912656 | decorators.py:78 | send_data_to_fm took 0.095 seconds
2023-12-20 15:35:56	
2023-12-20 08:35:56 | INFO | 10 | 140116199561552 | decorators.py:78 | send_data_to_fm took 0.098 seconds
2023-12-20 15:35:50	
2023-12-20 08:35:50 | INFO | 9 | 139681706912656 | decorators.py:78 | send_data_to_fm took 0.188 seconds
2023-12-20 15:35:45	
2023-12-20 08:35:45 | INFO | 10 | 139681706883408 | decorators.py:78 | send_data_to_fm took 0.018 seconds
2023-12-20 15:35:39	
2023-12-20 08:35:39 | INFO | 10 | 140116180991152 | decorators.py:78 | send_data_to_fm took 0.177 seconds
2023-12-20 15:35:29	
2023-12-20 08:35:29 | INFO | 10 | 139681706883408 | decorators.py:78 | send_data_to_fm took 0.020 seconds
2023-12-20 15:35:21	
2023-12-20 08:35:21 | INFO | 9 | 140116199573840 | decorators.py:78 | send_data_to_fm took 0.098 seconds
2023-12-20 15:35:06	
2023-12-20 08:35:06 | INFO | 9 | 139681758739632 | decorators.py:78 | send_data_to_fm took 0.099 seconds
2023-12-20 15:34:48	
2023-12-20 08:34:48 | INFO | 9 | 140116199573840 | decorators.py:78 | send_data_to_fm took 0.102 seconds
2023-12-20 15:34:46	
2023-12-20 08:34:46 | INFO | 10 | 140116199561552 | decorators.py:78 | send_data_to_fm took 0.102 seconds
2023-12-20 15:34:39	
2023-12-20 08:34:39 | INFO | 10 | 139681706883408 | decorators.py:78 | send_data_to_fm took 0.098 seconds
2023-12-20 15:34:38	
2023-12-20 08:34:38 | INFO | 10 | 140116199561552 | decorators.py:78 | send_data_to_fm took 0.101 seconds
2023-12-20 15:34:33	
2023-12-20 08:34:33 | INFO | 9 | 139681706912656 | decorators.py:78 | send_data_to_fm took 0.103 seconds
2023-12-20 15:34:23	
2023-12-20 08:34:23 | INFO | 10 | 140116199561552 | decorators.py:78 | send_data_to_fm took 0.098 seconds
2023-12-20 15:34:22	
2023-12-20 08:34:22 | INFO | 10 | 139681706883408 | decorators.py:78 | send_data_to_fm took 0.097 seconds
2023-12-20 15:34:19	
2023-12-20 08:34:19 | INFO | 10 | 139681706883408 | decorators.py:78 | send_data_to_fm took 0.099 seconds
2023-12-20 15:34:15	
2023-12-20 08:34:15 | INFO | 9 | 140116199573840 | decorators.py:78 | send_data_to_fm took 0.101 seconds
2023-12-20 15:34:13	
2023-12-20 08:34:13 | INFO | 10 | 140116199561552 | decorators.py:78 | send_data_to_fm took 0.100 seconds
2023-12-20 15:34:08	
2023-12-20 08:34:08 | INFO | 10 | 139681706883408 | decorators.py:78 | send_data_to_fm took 0.092 seconds
2023-12-20 15:34:02	
2023-12-20 08:34:02 | INFO | 9 | 139681706912656 | decorators.py:78 | send_data_to_fm took 0.103 seconds
2023-12-20 15:34:02	
2023-12-20 08:34:02 | INFO | 10 | 140116199561552 | decorators.py:78 | send_data_to_fm took 0.099 seconds
2023-12-20 15:33:59	
2023-12-20 08:33:59 | INFO | 10 | 140116199561552 | decorators.py:78 | send_data_to_fm took 0.096 seconds
2023-12-20 15:33:58	
2023-12-20 08:33:58 | INFO | 9 | 139681706912656 | decorators.py:78 | send_data_to_fm took 0.104 seconds
2023-12-20 15:33:58	
2023-12-20 08:33:58 | INFO | 10 | 140116199561552 | decorators.py:78 | send_data_to_fm took 0.088 seconds
2023-12-20 15:33:53	
2023-12-20 08:33:53 | INFO | 10 | 139681706883408 | decorators.py:78 | send_data_to_fm took 0.100 seconds
2023-12-20 15:33:51	
2023-12-20 08:33:51 | INFO | 10 | 140116199561552 | decorators.py:78 | send_data_to_fm took 0.099 seconds
2023-12-20 15:33:48	
2023-12-20 08:33:48 | INFO | 9 | 139681758739632 | decorators.py:78 | send_data_to_fm took 0.101 seconds
2023-12-20 15:33:39	
2023-12-20 08:33:39 | INFO | 10 | 140116199561552 | decorators.py:78 | send_data_to_fm took 0.187 seconds
2023-12-20 15:33:38	
2023-12-20 08:33:38 | INFO | 10 | 140116199561552 | decorators.py:78 | send_data_to_fm took 0.018 seconds
2023-12-20 15:33:35	
2023-12-20 08:33:35 | INFO | 9 | 139681706912656 | decorators.py:78 | send_data_to_fm took 0.099 seconds
2023-12-20 15:33:30	
2023-12-20 08:33:30 | INFO | 10 | 139681758751632 | decorators.py:78 | send_data_to_fm took 0.101 seconds
2023-12-20 15:33:17	
2023-12-20 08:33:17 | INFO | 9 | 139681706912656 | decorators.py:78 | send_data_to_fm took 0.101 seconds
2023-12-20 15:33:15	
2023-12-20 08:33:15 | INFO | 10 | 140116199561552 | decorators.py:78 | send_data_to_fm took 0.109 seconds
2023-12-20 15:33:15	
2023-12-20 08:33:15 | INFO | 10 | 140116199561552 | decorators.py:78 | send_data_to_fm took 0.099 seconds
2023-12-20 15:33:10	
2023-12-20 08:33:10 | INFO | 9 | 139681706912656 | decorators.py:78 | send_data_to_fm took 0.195 seconds
2023-12-20 15:33:09	
2023-12-20 08:33:09 | INFO | 10 | 140116180991152 | decorators.py:78 | send_data_to_fm took 0.104 seconds
2023-12-20 15:33:06	
2023-12-20 08:33:06 | INFO | 9 | 139681706912656 | decorators.py:78 | send_data_to_fm took 0.103 seconds
2023-12-20 15:32:55	
2023-12-20 08:32:55 | INFO | 10 | 139681706883408 | decorators.py:78 | send_data_to_fm took 0.098 seconds
2023-12-20 15:32:50	
2023-12-20 08:32:50 | INFO | 9 | 139681758739632 | decorators.py:78 | send_data_to_fm took 0.092 seconds
2023-12-20 15:32:49	
2023-12-20 08:32:49 | INFO | 9 | 140116199573840 | decorators.py:78 | send_data_to_fm took 0.102 seconds
2023-12-20 15:32:35	
2023-12-20 08:32:35 | INFO | 9 | 139681706912656 | decorators.py:78 | send_data_to_fm took 0.099 seconds
2023-12-20 15:32:32	
2023-12-20 08:32:32 | INFO | 9 | 140116199573840 | decorators.py:78 | send_data_to_fm took 0.188 seconds
2023-12-20 15:32:24	
2023-12-20 08:32:24 | INFO | 9 | 139681706912656 | decorators.py:78 | send_data_to_fm took 0.097 seconds
2023-12-20 15:32:15	
2023-12-20 08:32:15 | INFO | 10 | 139681758751632 | decorators.py:78 | send_data_to_fm took 0.100 seconds
2023-12-20 15:32:13	
2023-12-20 08:32:13 | INFO | 10 | 139681758751632 | decorators.py:78 | send_data_to_fm took 0.187 seconds
2023-12-20 15:32:12	
2023-12-20 08:32:12 | INFO | 10 | 139681758751632 | decorators.py:78 | send_data_to_fm took 0.099 seconds
2023-12-20 15:32:10	
2023-12-20 08:32:10 | INFO | 9 | 140116164271856 | decorators.py:78 | send_data_to_fm took 0.188 seconds
2023-12-20 15:32:04	
2023-12-20 08:32:04 | INFO | 10 | 139681758751344 | decorators.py:78 | send_data_to_fm took 0.016 seconds
2023-12-20 15:32:02	
2023-12-20 08:32:02 | INFO | 9 | 140116199573840 | decorators.py:78 | send_data_to_fm took 0.101 seconds
2023-12-20 15:32:02	
2023-12-20 08:32:02 | INFO | 10 | 139681758751344 | decorators.py:78 | send_data_to_fm took 0.180 seconds
2023-12-20 15:31:53	
2023-12-20 08:31:53 | INFO | 9 | 139681706912656 | decorators.py:78 | send_data_to_fm took 0.100 seconds
2023-12-20 15:31:50	
2023-12-20 08:31:50 | INFO | 9 | 140116164271568 | decorators.py:78 | send_data_to_fm took 0.103 seconds
2023-12-20 15:31:49	
2023-12-20 08:31:49 | INFO | 10 | 139681758751344 | decorators.py:78 | send_data_to_fm took 0.171 seconds
2023-12-20 15:31:29	
2023-12-20 08:31:29 | INFO | 10 | 139681706883408 | decorators.py:78 | send_data_to_fm took 0.110 seconds
2023-12-20 15:31:27	
2023-12-20 08:31:27 | INFO | 10 | 140116180991152 | decorators.py:78 | send_data_to_fm took 0.098 seconds
2023-12-20 15:31:26	
2023-12-20 08:31:26 | INFO | 10 | 139681706883408 | decorators.py:78 | send_data_to_fm took 0.100 seconds
2023-12-20 15:31:14	
2023-12-20 08:31:14 | INFO | 9 | 140116199573840 | decorators.py:78 | send_data_to_fm took 0.103 seconds
2023-12-20 15:31:05	
2023-12-20 08:31:05 | INFO | 10 | 140116199561552 | decorators.py:78 | send_data_to_fm took 0.097 seconds
2023-12-20 15:30:55	
2023-12-20 08:30:55 | INFO | 9 | 139681706912656 | decorators.py:78 | send_data_to_fm took 0.097 seconds
2023-12-20 15:30:52	
2023-12-20 08:30:52 | INFO | 9 | 140116199573840 | decorators.py:78 | send_data_to_fm took 0.103 seconds
2023-12-20 15:30:39	
2023-12-20 08:30:39 | INFO | 9 | 139681706912656 | decorators.py:78 | send_data_to_fm took 0.095 seconds
2023-12-20 15:30:30	
2023-12-20 08:30:30 | INFO | 10 | 140116180991152 | decorators.py:78 | send_data_to_fm took 0.099 seconds
2023-12-20 15:30:19	
2023-12-20 08:30:19 | INFO | 10 | 139681706883408 | decorators.py:78 | send_data_to_fm took 0.109 seconds
2023-12-20 15:30:17	
2023-12-20 08:30:17 | INFO | 10 | 139681706883408 | decorators.py:78 | send_data_to_fm took 0.106 seconds
2023-12-20 15:30:14	
2023-12-20 08:30:14 | INFO | 10 | 140116199561552 | decorators.py:78 | send_data_to_fm took 0.101 seconds
2023-12-20 15:30:03	
2023-12-20 08:30:03 | INFO | 10 | 140116199561552 | decorators.py:78 | send_data_to_fm took 0.099 seconds
2023-12-20 15:29:56	
2023-12-20 08:29:56 | INFO | 9 | 139681758739344 | decorators.py:78 | send_data_to_fm took 0.186 seconds
2023-12-20 15:29:54	
2023-12-20 08:29:54 | INFO | 9 | 139681758739344 | decorators.py:78 | send_data_to_fm took 0.098 seconds
2023-12-20 15:29:53	
2023-12-20 08:29:53 | INFO | 9 | 140116199573840 | decorators.py:78 | send_data_to_fm took 0.097 seconds
2023-12-20 15:29:52	
2023-12-20 08:29:52 | INFO | 9 | 139681758739344 | decorators.py:78 | send_data_to_fm took 0.097 seconds
2023-12-20 15:29:46	
2023-12-20 08:29:46 | INFO | 9 | 139681706912656 | decorators.py:78 | send_data_to_fm took 0.099 seconds
2023-12-20 15:29:44	
2023-12-20 08:29:44 | INFO | 10 | 140116199561552 | decorators.py:78 | send_data_to_fm took 0.191 seconds
2023-12-20 15:29:41	
2023-12-20 08:29:41 | INFO | 10 | 139681758751632 | decorators.py:78 | send_data_to_fm took 0.186 seconds
2023-12-20 15:29:36	
2023-12-20 08:29:36 | INFO | 9 | 140116199573840 | decorators.py:78 | send_data_to_fm took 0.099 seconds
2023-12-20 15:29:34	
2023-12-20 08:29:34 | INFO | 9 | 140116199573840 | decorators.py:78 | send_data_to_fm took 0.099 seconds
2023-12-20 15:29:32	
2023-12-20 08:29:32 | INFO | 9 | 140116199573840 | decorators.py:78 | send_data_to_fm took 0.100 seconds
2023-12-20 15:29:32	
2023-12-20 08:29:32 | INFO | 10 | 139681758751632 | decorators.py:78 | send_data_to_fm took 0.101 seconds
2023-12-20 15:29:27	
2023-12-20 08:29:27 | INFO | 9 | 139681706912656 | decorators.py:78 | send_data_to_fm took 0.102 seconds
2023-12-20 15:29:26	
2023-12-20 08:29:26 | INFO | 9 | 139681706912656 | decorators.py:78 | send_data_to_fm took 0.098 seconds
2023-12-20 15:29:24	
2023-12-20 08:29:24 | INFO | 10 | 140116199561552 | decorators.py:78 | send_data_to_fm took 0.111 seconds
2023-12-20 15:29:24	
2023-12-20 08:29:24 | INFO | 10 | 140116199561552 | decorators.py:78 | send_data_to_fm took 0.097 seconds
2023-12-20 15:29:21	
2023-12-20 08:29:21 | INFO | 10 | 139681758751632 | decorators.py:78 | send_data_to_fm took 0.087 seconds
2023-12-20 15:29:07	
2023-12-20 08:29:07 | INFO | 10 | 140116199561552 | decorators.py:78 | send_data_to_fm took 0.187 seconds
2023-12-20 15:29:06	
2023-12-20 08:29:06 | INFO | 10 | 139681706883408 | decorators.py:78 | send_data_to_fm took 0.188 seconds
2023-12-20 15:28:51	
2023-12-20 08:28:51 | INFO | 9 | 139681758739632 | decorators.py:78 | send_data_to_fm took 0.098 seconds
2023-12-20 15:28:45	
2023-12-20 08:28:45 | INFO | 9 | 140116199573840 | decorators.py:78 | send_data_to_fm took 0.103 seconds
2023-12-20 15:28:31	
2023-12-20 08:28:31 | INFO | 9 | 139681758739632 | decorators.py:78 | send_data_to_fm took 0.183 seconds
2023-12-20 15:28:31	
2023-12-20 08:28:31 | INFO | 9 | 140116199573840 | decorators.py:78 | send_data_to_fm took 0.184 seconds
2023-12-20 15:28:25	
2023-12-20 08:28:25 | INFO | 9 | 139681706912656 | decorators.py:78 | send_data_to_fm took 0.098 seconds
2023-12-20 15:28:23	
2023-12-20 08:28:23 | INFO | 9 | 139681706912656 | decorators.py:78 | send_data_to_fm took 0.107 seconds
2023-12-20 15:28:23	
2023-12-20 08:28:23 | INFO | 9 | 139681706912656 | decorators.py:78 | send_data_to_fm took 0.098 seconds
2023-12-20 15:28:22	
2023-12-20 08:28:22 | INFO | 10 | 140116199561552 | decorators.py:78 | send_data_to_fm took 0.104 seconds
2023-12-20 15:28:09	
2023-12-20 08:28:09 | INFO | 10 | 139681706883408 | decorators.py:78 | send_data_to_fm took 0.104 seconds
2023-12-20 15:28:03	
2023-12-20 08:28:03 | INFO | 9 | 139681758739632 | decorators.py:78 | send_data_to_fm took 0.097 seconds
2023-12-20 15:28:02	
2023-12-20 08:28:02 | INFO | 9 | 139681758739632 | decorators.py:78 | send_data_to_fm took 0.103 seconds
2023-12-20 15:28:02	
2023-12-20 08:28:02 | INFO | 9 | 140116164270704 | decorators.py:78 | send_data_to_fm took 0.099 seconds
2023-12-20 15:27:59	
2023-12-20 08:27:59 | INFO | 9 | 140116164270704 | decorators.py:78 | send_data_to_fm took 0.102 seconds
2023-12-20 15:27:58	
2023-12-20 08:27:58 | INFO | 10 | 139681758751344 | decorators.py:78 | send_data_to_fm took 0.102 seconds
2023-12-20 15:27:55	
2023-12-20 08:27:55 | INFO | 10 | 140116180990864 | decorators.py:78 | send_data_to_fm took 0.103 seconds
2023-12-20 15:27:54	
2023-12-20 08:27:54 | INFO | 9 | 139681758739632 | decorators.py:78 | send_data_to_fm took 0.112 seconds
2023-12-20 15:27:50	
2023-12-20 08:27:50 | INFO | 9 | 140116199573840 | decorators.py:78 | send_data_to_fm took 0.184 seconds
2023-12-20 15:27:49	
2023-12-20 08:27:49 | INFO | 10 | 139681706883408 | decorators.py:78 | send_data_to_fm took 0.100 seconds
2023-12-20 15:27:47	
2023-12-20 08:27:47 | INFO | 10 | 139681706883408 | decorators.py:78 | send_data_to_fm took 0.182 seconds
2023-12-20 15:27:45	
2023-12-20 08:27:45 | INFO | 9 | 140116199573840 | decorators.py:78 | send_data_to_fm took 0.017 seconds
2023-12-20 15:27:44	
2023-12-20 08:27:44 | INFO | 10 | 139681706883408 | decorators.py:78 | send_data_to_fm took 0.100 seconds
2023-12-20 15:27:39	
2023-12-20 08:27:39 | INFO | 9 | 140116199573840 | decorators.py:78 | send_data_to_fm took 0.102 seconds
2023-12-20 15:27:35	
2023-12-20 08:27:35 | INFO | 9 | 139681706912656 | decorators.py:78 | send_data_to_fm took 0.180 seconds
2023-12-20 15:27:27	
2023-12-20 08:27:27 | INFO | 10 | 140116199561552 | decorators.py:78 | send_data_to_fm took 0.099 seconds
2023-12-20 15:27:25	
2023-12-20 08:27:25 | INFO | 10 | 140116199561552 | decorators.py:78 | send_data_to_fm took 0.189 seconds
2023-12-20 15:27:07	
2023-12-20 08:27:07 | INFO | 9 | 140116199573840 | decorators.py:78 | send_data_to_fm took 0.106 seconds
2023-12-20 15:27:07	
2023-12-20 08:27:07 | INFO | 9 | 140116199573840 | decorators.py:78 | send_data_to_fm took 0.179 seconds
2023-12-20 15:27:03	
2023-12-20 08:27:03 | INFO | 9 | 139681758739056 | decorators.py:78 | send_data_to_fm took 0.108 seconds
2023-12-20 15:27:03	
2023-12-20 08:27:03 | INFO | 9 | 139681758739344 | decorators.py:78 | send_data_to_fm took 0.195 seconds
2023-12-20 15:27:03	
2023-12-20 08:27:03 | INFO | 9 | 140116199573840 | decorators.py:78 | send_data_to_fm took 0.184 seconds
2023-12-20 15:27:03	
2023-12-20 08:27:03 | INFO | 10 | 139681758751344 | decorators.py:78 | send_data_to_fm took 0.298 seconds
2023-12-20 15:27:02	
2023-12-20 08:27:02 | INFO | 9 | 140116199573840 | decorators.py:78 | send_data_to_fm took 0.095 seconds
2023-12-20 15:26:57	
2023-12-20 08:26:57 | INFO | 9 | 140116199573840 | decorators.py:78 | send_data_to_fm took 0.106 seconds
2023-12-20 15:26:56	
2023-12-20 08:26:56 | INFO | 9 | 139681706912656 | decorators.py:78 | send_data_to_fm took 0.103 seconds
2023-12-20 15:26:48	
2023-12-20 08:26:48 | INFO | 9 | 140116164271568 | decorators.py:78 | send_data_to_fm took 0.186 seconds
2023-12-20 15:26:47	
2023-12-20 08:26:47 | INFO | 10 | 139681706883408 | decorators.py:78 | send_data_to_fm took 0.105 seconds
2023-12-20 15:26:42	
2023-12-20 08:26:42 | INFO | 10 | 140116180990864 | decorators.py:78 | send_data_to_fm took 0.105 seconds
2023-12-20 15:26:42	
2023-12-20 08:26:42 | INFO | 10 | 140116199561552 | decorators.py:78 | send_data_to_fm took 0.196 seconds
2023-12-20 15:26:34	
2023-12-20 08:26:34 | INFO | 10 | 139681706883408 | decorators.py:78 | send_data_to_fm took 0.102 seconds
2023-12-20 15:26:28	
2023-12-20 08:26:28 | INFO | 9 | 139681706912656 | decorators.py:78 | send_data_to_fm took 0.101 seconds
2023-12-20 15:26:26	
2023-12-20 08:26:26 | INFO | 9 | 140116199573840 | decorators.py:78 | send_data_to_fm took 0.185 seconds
2023-12-20 15:26:14	
2023-12-20 08:26:14 | INFO | 9 | 140116199573840 | decorators.py:78 | send_data_to_fm took 0.103 seconds
2023-12-20 15:25:58	
2023-12-20 08:25:58 | INFO | 9 | 139681706912656 | decorators.py:78 | send_data_to_fm took 0.098 seconds
2023-12-20 15:25:48	
2023-12-20 08:25:48 | INFO | 10 | 139681706883408 | decorators.py:78 | send_data_to_fm took 0.102 seconds
2023-12-20 15:25:45	
2023-12-20 08:25:45 | INFO | 9 | 140116199573840 | decorators.py:78 | send_data_to_fm took 0.105 seconds
2023-12-20 15:25:36	
2023-12-20 08:25:36 | INFO | 9 | 139681706912656 | decorators.py:78 | send_data_to_fm took 0.184 seconds
2023-12-20 15:25:28	
2023-12-20 08:25:28 | INFO | 9 | 139681706912656 | decorators.py:78 | send_data_to_fm took 0.105 seconds
2023-12-20 15:25:27	
2023-12-20 08:25:27 | INFO | 9 | 139681706912656 | decorators.py:78 | send_data_to_fm took 0.099 seconds
2023-12-20 15:25:25	
2023-12-20 08:25:25 | INFO | 10 | 140116199561552 | decorators.py:78 | send_data_to_fm took 0.196 seconds
2023-12-20 15:25:25	
2023-12-20 08:25:25 | INFO | 10 | 140116199561552 | decorators.py:78 | send_data_to_fm took 0.100 seconds
2023-12-20 15:25:20	
2023-12-20 08:25:20 | INFO | 10 | 139681706883408 | decorators.py:78 | send_data_to_fm took 0.193 seconds
2023-12-20 15:25:19	
2023-12-20 08:25:19 | INFO | 10 | 139681706883408 | decorators.py:78 | send_data_to_fm took 0.106 seconds
2023-12-20 15:25:18	
2023-12-20 08:25:18 | INFO | 10 | 139681706883408 | decorators.py:78 | send_data_to_fm took 0.100 seconds
2023-12-20 15:25:17	
2023-12-20 08:25:17 | INFO | 10 | 140116199561552 | decorators.py:78 | send_data_to_fm took 0.096 seconds
2023-12-20 15:25:11	
2023-12-20 08:25:11 | INFO | 10 | 140116199561552 | decorators.py:78 | send_data_to_fm took 0.102 seconds
2023-12-20 15:25:07	
2023-12-20 08:25:07 | INFO | 9 | 139681758739344 | decorators.py:78 | send_data_to_fm took 0.114 seconds
2023-12-20 15:25:07	
2023-12-20 08:25:07 | INFO | 10 | 139681706883408 | decorators.py:78 | send_data_to_fm took 0.394 seconds
2023-12-20 15:25:06	
2023-12-20 08:25:06 | INFO | 10 | 140116199561552 | decorators.py:78 | send_data_to_fm took 0.099 seconds
2023-12-20 15:25:05	
2023-12-20 08:25:05 | INFO | 10 | 139681706883408 | decorators.py:78 | send_data_to_fm took 0.105 seconds
2023-12-20 15:24:59	
2023-12-20 08:24:59 | INFO | 9 | 140116199573840 | decorators.py:78 | send_data_to_fm took 0.186 seconds
2023-12-20 15:24:57	
2023-12-20 08:24:57 | INFO | 9 | 139681706912656 | decorators.py:78 | send_data_to_fm took 0.098 seconds
2023-12-20 15:24:56	
2023-12-20 08:24:56 | INFO | 9 | 139681706912656 | decorators.py:78 | send_data_to_fm took 0.096 seconds
2023-12-20 15:24:51	
2023-12-20 08:24:51 | INFO | 10 | 140116180991728 | decorators.py:78 | send_data_to_fm took 0.197 seconds
2023-12-20 15:24:51	
2023-12-20 08:24:51 | INFO | 9 | 140116199573840 | decorators.py:78 | send_data_to_fm took 0.195 seconds
2023-12-20 15:24:47	
2023-12-20 08:24:47 | INFO | 9 | 140116199573840 | decorators.py:78 | send_data_to_fm took 0.103 seconds
2023-12-20 15:24:46	
2023-12-20 08:24:46 | INFO | 10 | 139681706883408 | decorators.py:78 | send_data_to_fm took 0.185 seconds
2023-12-20 15:24:46	
2023-12-20 08:24:46 | INFO | 9 | 140116199573840 | decorators.py:78 | send_data_to_fm took 0.104 seconds
2023-12-20 15:24:39	
2023-12-20 08:24:39 | INFO | 10 | 140116180991728 | decorators.py:78 | send_data_to_fm took 0.097 seconds
2023-12-20 15:24:30	
2023-12-20 08:24:30 | INFO | 9 | 139681706912656 | decorators.py:78 | send_data_to_fm took 0.096 seconds
2023-12-20 15:24:29	
2023-12-20 08:24:29 | INFO | 9 | 140116199573840 | decorators.py:78 | send_data_to_fm took 0.093 seconds
2023-12-20 15:24:28	
2023-12-20 08:24:28 | INFO | 9 | 139681706912656 | decorators.py:78 | send_data_to_fm took 0.097 seconds
2023-12-20 15:24:27	
2023-12-20 08:24:27 | INFO | 9 | 140116199573840 | decorators.py:78 | send_data_to_fm took 0.185 seconds
2023-12-20 15:24:27	
2023-12-20 08:24:27 | INFO | 9 | 139681706912656 | decorators.py:78 | send_data_to_fm took 0.100 seconds
2023-12-20 15:24:22	
2023-12-20 08:24:22 | INFO | 10 | 140116199561552 | decorators.py:78 | send_data_to_fm took 0.291 seconds
2023-12-20 15:24:21	
2023-12-20 08:24:21 | INFO | 9 | 139681706912656 | decorators.py:78 | send_data_to_fm took 0.186 seconds
2023-12-20 15:24:20	
2023-12-20 08:24:20 | INFO | 9 | 139681706912656 | decorators.py:78 | send_data_to_fm took 0.100 seconds
2023-12-20 15:24:19	
2023-12-20 08:24:19 | INFO | 10 | 140116199561552 | decorators.py:78 | send_data_to_fm took 0.100 seconds
2023-12-20 15:24:11	
2023-12-20 08:24:11 | INFO | 10 | 140116199561552 | decorators.py:78 | send_data_to_fm took 0.189 seconds
2023-12-20 15:24:08	
2023-12-20 08:24:08 | INFO | 10 | 140116199561552 | decorators.py:78 | send_data_to_fm took 0.106 seconds
2023-12-20 15:24:07	
2023-12-20 08:24:07 | INFO | 10 | 140116199561552 | decorators.py:78 | send_data_to_fm took 0.182 seconds
2023-12-20 15:24:02	
2023-12-20 08:24:02 | INFO | 10 | 140116199561552 | decorators.py:78 | send_data_to_fm took 0.105 seconds
2023-12-20 15:24:01	
2023-12-20 08:24:01 | INFO | 10 | 139681758751632 | decorators.py:78 | send_data_to_fm took 0.103 seconds
2023-12-20 15:24:01	
2023-12-20 08:24:01 | INFO | 9 | 139681758739344 | decorators.py:78 | send_data_to_fm took 0.396 seconds
2023-12-20 15:23:49	
2023-12-20 08:23:49 | INFO | 10 | 140116199561552 | decorators.py:78 | send_data_to_fm took 0.098 seconds
2023-12-20 15:23:47	
2023-12-20 08:23:47 | INFO | 10 | 139681758751344 | decorators.py:78 | send_data_to_fm took 0.102 seconds
2023-12-20 15:23:42	
2023-12-20 08:23:42 | INFO | 9 | 140116199573840 | decorators.py:78 | send_data_to_fm took 0.186 seconds
2023-12-20 15:23:40	
2023-12-20 08:23:40 | INFO | 10 | 139681758751344 | decorators.py:78 | send_data_to_fm took 0.094 seconds
2023-12-20 15:23:29	
2023-12-20 08:23:29 | INFO | 10 | 139681758751344 | decorators.py:78 | send_data_to_fm took 0.097 seconds
2023-12-20 15:23:28	
2023-12-20 08:23:28 | INFO | 10 | 139681758751344 | decorators.py:78 | send_data_to_fm took 0.096 seconds
2023-12-20 15:23:27	
2023-12-20 08:23:27 | INFO | 10 | 139681758751344 | decorators.py:78 | send_data_to_fm took 0.093 seconds
2023-12-20 15:23:18	
2023-12-20 08:23:18 | INFO | 10 | 139681706883408 | decorators.py:78 | send_data_to_fm took 0.175 seconds
2023-12-20 15:23:18	
2023-12-20 08:23:18 | INFO | 10 | 139681706883408 | decorators.py:78 | send_data_to_fm took 0.101 seconds
2023-12-20 15:23:17	
2023-12-20 08:23:17 | INFO | 9 | 139681706912656 | decorators.py:78 | send_data_to_fm took 0.304 seconds
2023-12-20 15:23:17	
2023-12-20 08:23:17 | INFO | 10 | 140116199561552 | decorators.py:78 | send_data_to_fm took 0.101 seconds
2023-12-20 15:23:16	
2023-12-20 08:23:16 | INFO | 10 | 140116199561552 | decorators.py:78 | send_data_to_fm took 0.103 seconds
2023-12-20 15:23:16	
2023-12-20 08:23:16 | INFO | 9 | 139681706912656 | decorators.py:78 | send_data_to_fm took 0.187 seconds
2023-12-20 15:23:16	
2023-12-20 08:23:16 | INFO | 9 | 139681706912656 | decorators.py:78 | send_data_to_fm took 0.099 seconds
2023-12-20 15:23:16	
2023-12-20 08:23:16 | INFO | 10 | 139681706883408 | decorators.py:78 | send_data_to_fm took 0.304 seconds
2023-12-20 15:23:15	
2023-12-20 08:23:15 | INFO | 10 | 140116199561552 | decorators.py:78 | send_data_to_fm took 0.182 seconds
2023-12-20 15:23:14	
2023-12-20 08:23:14 | INFO | 10 | 139681706883408 | decorators.py:78 | send_data_to_fm took 0.100 seconds
2023-12-20 15:23:14	
2023-12-20 08:23:14 | INFO | 10 | 140116199561552 | decorators.py:78 | send_data_to_fm took 0.104 seconds
2023-12-20 15:23:14	
2023-12-20 08:23:14 | INFO | 10 | 140116180990864 | decorators.py:78 | send_data_to_fm took 0.290 seconds
2023-12-20 15:23:14	
2023-12-20 08:23:14 | INFO | 10 | 139681706883408 | decorators.py:78 | send_data_to_fm took 0.106 seconds
2023-12-20 15:23:14	
2023-12-20 08:23:14 | INFO | 9 | 140116199573840 | decorators.py:78 | send_data_to_fm took 0.306 seconds
2023-12-20 15:23:13	
2023-12-20 08:23:13 | INFO | 9 | 139681758739344 | decorators.py:78 | send_data_to_fm took 0.187 seconds
2023-12-20 15:23:13	
2023-12-20 08:23:13 | INFO | 9 | 140116199573840 | decorators.py:78 | send_data_to_fm took 0.104 seconds
2023-12-20 15:23:13	
2023-12-20 08:23:13 | INFO | 10 | 140116180990864 | decorators.py:78 | send_data_to_fm took 0.202 seconds
2023-12-20 15:23:11	
2023-12-20 08:23:11 | INFO | 10 | 140116180990864 | decorators.py:78 | send_data_to_fm took 0.206 seconds
2023-12-20 15:23:11	
2023-12-20 08:23:11 | INFO | 10 | 139681706883408 | decorators.py:78 | send_data_to_fm took 0.200 seconds
2023-12-20 15:23:11	
2023-12-20 08:23:11 | INFO | 9 | 139681462718544 | decorators.py:78 | send_data_to_fm took 0.205 seconds
2023-12-20 15:23:10	
2023-12-20 08:23:10 | INFO | 9 | 139681758739344 | decorators.py:78 | send_data_to_fm took 0.396 seconds
2023-12-20 15:23:10	
2023-12-20 08:23:10 | INFO | 10 | 140116180990864 | decorators.py:78 | send_data_to_fm took 0.186 seconds
2023-12-20 15:23:02	
2023-12-20 08:23:02 | INFO | 9 | 140116199573840 | decorators.py:78 | send_data_to_fm took 0.096 seconds
2023-12-20 15:23:01	
2023-12-20 08:23:01 | INFO | 9 | 139681758739344 | decorators.py:78 | send_data_to_fm took 0.100 seconds
2023-12-20 15:22:55	
2023-12-20 08:22:55 | INFO | 9 | 140116199573840 | decorators.py:78 | send_data_to_fm took 0.097 seconds
2023-12-20 15:22:54	
2023-12-20 08:22:54 | INFO | 9 | 139681706912656 | decorators.py:78 | send_data_to_fm took 0.101 seconds
2023-12-20 15:22:52	
2023-12-20 08:22:52 | INFO | 9 | 139681706912656 | decorators.py:78 | send_data_to_fm took 0.092 seconds
2023-12-20 15:22:51	
2023-12-20 08:22:51 | INFO | 9 | 140116199573840 | decorators.py:78 | send_data_to_fm took 0.100 seconds
2023-12-20 15:22:50	
2023-12-20 08:22:50 | INFO | 9 | 140116199573840 | decorators.py:78 | send_data_to_fm took 0.098 seconds
2023-12-20 15:22:50	
2023-12-20 08:22:50 | INFO | 9 | 139681706912656 | decorators.py:78 | send_data_to_fm took 0.195 seconds
2023-12-20 15:22:50	
2023-12-20 08:22:50 | INFO | 9 | 139681706912656 | decorators.py:78 | send_data_to_fm took 0.096 seconds
2023-12-20 15:22:49	
2023-12-20 08:22:49 | INFO | 9 | 139681706912656 | decorators.py:78 | send_data_to_fm took 0.098 seconds
2023-12-20 15:22:48	
2023-12-20 08:22:48 | INFO | 9 | 140116199573840 | decorators.py:78 | send_data_to_fm took 0.187 seconds
2023-12-20 15:22:43	
2023-12-20 08:22:43 | INFO | 10 | 140116199561552 | decorators.py:78 | send_data_to_fm took 0.181 seconds
2023-12-20 15:22:42	
2023-12-20 08:22:42 | INFO | 9 | 139681706912656 | decorators.py:78 | send_data_to_fm took 0.102 seconds
2023-12-20 15:22:33	
2023-12-20 08:22:33 | INFO | 9 | 140116199573840 | decorators.py:78 | send_data_to_fm took 0.190 seconds
2023-12-20 15:22:33	
2023-12-20 08:22:33 | INFO | 9 | 139681706912656 | decorators.py:78 | send_data_to_fm took 0.093 seconds
2023-12-20 15:22:30	
2023-12-20 08:22:30 | INFO | 10 | 140116199561552 | decorators.py:78 | send_data_to_fm took 0.099 seconds
2023-12-20 15:22:28	
2023-12-20 08:22:28 | INFO | 10 | 140116199561552 | decorators.py:78 | send_data_to_fm took 0.104 seconds
2023-12-20 15:22:27	
2023-12-20 08:22:27 | INFO | 9 | 139681706912656 | decorators.py:78 | send_data_to_fm took 0.103 seconds
2023-12-20 15:22:25	
2023-12-20 08:22:25 | INFO | 10 | 140116199561552 | decorators.py:78 | send_data_to_fm took 0.099 seconds
2023-12-20 15:22:24	
2023-12-20 08:22:24 | INFO | 9 | 139681706912656 | decorators.py:78 | send_data_to_fm took 0.098 seconds
2023-12-20 15:22:24	
2023-12-20 08:22:24 | INFO | 10 | 140116199561552 | decorators.py:78 | send_data_to_fm took 0.098 seconds
2023-12-20 15:22:22	
2023-12-20 08:22:22 | INFO | 9 | 140116164271568 | decorators.py:78 | send_data_to_fm took 0.101 seconds
2023-12-20 15:22:13	
2023-12-20 08:22:13 | INFO | 10 | 139681758751632 | decorators.py:78 | send_data_to_fm took 0.098 seconds
2023-12-20 15:22:07	
2023-12-20 08:22:07 | INFO | 9 | 140116199573840 | decorators.py:78 | send_data_to_fm took 0.105 seconds
2023-12-20 15:22:05	
2023-12-20 08:22:05 | INFO | 9 | 139681706912656 | decorators.py:78 | send_data_to_fm took 0.098 seconds
2023-12-20 15:21:42	
2023-12-20 08:21:42 | INFO | 10 | 139681758751632 | decorators.py:78 | send_data_to_fm took 0.099 seconds
2023-12-20 15:21:40	
2023-12-20 08:21:40 | INFO | 10 | 140116180990864 | decorators.py:78 | send_data_to_fm took 0.105 seconds
2023-12-20 15:21:32	
2023-12-20 08:21:32 | INFO | 9 | 139681462432112 | decorators.py:78 | send_data_to_fm took 0.102 seconds
2023-12-20 15:21:31	
2023-12-20 08:21:31 | INFO | 10 | 140116199561552 | decorators.py:78 | send_data_to_fm took 0.100 seconds
2023-12-20 15:21:22	
2023-12-20 08:21:22 | INFO | 9 | 140116199573840 | decorators.py:78 | send_data_to_fm took 0.099 seconds
2023-12-20 15:21:20	
2023-12-20 08:21:20 | INFO | 9 | 139681758739344 | decorators.py:78 | send_data_to_fm took 0.092 seconds
2023-12-20 15:21:19	
2023-12-20 08:21:19 | INFO | 9 | 139681758739344 | decorators.py:78 | send_data_to_fm took 0.100 seconds
2023-12-20 15:21:12	
2023-12-20 08:21:12 | INFO | 9 | 139681758739344 | decorators.py:78 | send_data_to_fm took 0.093 seconds
2023-12-20 15:21:11	
2023-12-20 08:21:11 | INFO | 10 | 140116180991728 | decorators.py:78 | send_data_to_fm took 0.098 seconds
2023-12-20 15:21:01	
2023-12-20 08:21:01 | INFO | 9 | 139681758739344 | decorators.py:78 | send_data_to_fm took 0.182 seconds
2023-12-20 15:21:00	
2023-12-20 08:21:00 | INFO | 9 | 140116164270704 | decorators.py:78 | send_data_to_fm took 0.193 seconds
2023-12-20 15:20:59	
2023-12-20 08:20:59 | INFO | 9 | 139681758739344 | decorators.py:78 | send_data_to_fm took 0.097 seconds
2023-12-20 15:20:56	
2023-12-20 08:20:56 | INFO | 9 | 139681758739344 | decorators.py:78 | send_data_to_fm took 0.101 seconds
2023-12-20 15:20:50	
2023-12-20 08:20:50 | INFO | 10 | 140116199561552 | decorators.py:78 | send_data_to_fm took 0.100 seconds
2023-12-20 15:20:49	
2023-12-20 08:20:49 | INFO | 9 | 139681706912656 | decorators.py:78 | send_data_to_fm took 0.103 seconds
2023-12-20 15:20:48	
2023-12-20 08:20:48 | INFO | 10 | 140116199561552 | decorators.py:78 | send_data_to_fm took 0.100 seconds
2023-12-20 15:20:47	
2023-12-20 08:20:47 | INFO | 9 | 139681706912656 | decorators.py:78 | send_data_to_fm took 0.100 seconds
2023-12-20 15:20:36	
2023-12-20 08:20:36 | INFO | 9 | 140116199573840 | decorators.py:78 | send_data_to_fm took 0.108 seconds
2023-12-20 15:20:36	
2023-12-20 08:20:36 | INFO | 9 | 140116199573840 | decorators.py:78 | send_data_to_fm took 0.104 seconds
2023-12-20 15:20:34	
2023-12-20 08:20:34 | INFO | 9 | 139681706912656 | decorators.py:78 | send_data_to_fm took 0.104 seconds
2023-12-20 15:20:29	
2023-12-20 08:20:29 | INFO | 10 | 139681706883408 | decorators.py:78 | send_data_to_fm took 0.106 seconds
2023-12-20 15:20:28	
2023-12-20 08:20:28 | INFO | 9 | 140116199573840 | decorators.py:78 | send_data_to_fm took 0.099 seconds
2023-12-20 15:20:16	
2023-12-20 08:20:16 | INFO | 10 | 139681758751632 | decorators.py:78 | send_data_to_fm took 0.107 seconds
2023-12-20 15:20:14	
2023-12-20 08:20:14 | INFO | 9 | 139681758739344 | decorators.py:78 | send_data_to_fm took 0.181 seconds
2023-12-20 15:20:09	
2023-12-20 08:20:09 | INFO | 10 | 139681706883408 | decorators.py:78 | send_data_to_fm took 0.106 seconds
2023-12-20 15:19:55	
2023-12-20 08:19:55 | INFO | 10 | 140116199561552 | decorators.py:78 | send_data_to_fm took 0.182 seconds
2023-12-20 15:19:49	
2023-12-20 08:19:49 | INFO | 10 | 140116199561552 | decorators.py:78 | send_data_to_fm took 0.098 seconds
2023-12-20 15:19:47	
2023-12-20 08:19:47 | INFO | 9 | 139681758739344 | decorators.py:78 | send_data_to_fm took 0.101 seconds
2023-12-20 15:19:40	
2023-12-20 08:19:40 | INFO | 9 | 139681758739344 | decorators.py:78 | send_data_to_fm took 0.196 seconds
2023-12-20 15:19:38	
2023-12-20 08:19:38 | INFO | 9 | 140116199573840 | decorators.py:78 | send_data_to_fm took 0.199 seconds
2023-12-20 15:19:38	
2023-12-20 08:19:38 | INFO | 10 | 140116199561552 | decorators.py:78 | send_data_to_fm took 0.298 seconds
2023-12-20 15:19:37	
2023-12-20 08:19:37 | INFO | 9 | 139681758739344 | decorators.py:78 | send_data_to_fm took 0.098 seconds
2023-12-20 15:19:34	
2023-12-20 08:19:34 | INFO | 10 | 139681706883408 | decorators.py:78 | send_data_to_fm took 0.097 seconds
2023-12-20 15:19:27	
2023-12-20 08:19:27 | INFO | 10 | 140116199561552 | decorators.py:78 | send_data_to_fm took 0.108 seconds
2023-12-20 15:19:21	
2023-12-20 08:19:21 | INFO | 9 | 139681758739344 | decorators.py:78 | send_data_to_fm took 0.100 seconds
2023-12-20 15:19:20	
2023-12-20 08:19:20 | INFO | 9 | 139681758739344 | decorators.py:78 | send_data_to_fm took 0.183 seconds
2023-12-20 15:19:18	
2023-12-20 08:19:18 | INFO | 10 | 140116199561552 | decorators.py:78 | send_data_to_fm took 0.179 seconds
2023-12-20 15:19:17	
2023-12-20 08:19:17 | INFO | 9 | 139681758739344 | decorators.py:78 | send_data_to_fm took 0.097 seconds
2023-12-20 15:19:17	
2023-12-20 08:19:17 | INFO | 10 | 140116199561552 | decorators.py:78 | send_data_to_fm took 0.096 seconds
2023-12-20 15:19:02	
2023-12-20 08:19:02 | INFO | 9 | 139681758739344 | decorators.py:78 | send_data_to_fm took 0.099 seconds
2023-12-20 15:19:00	
2023-12-20 08:19:00 | INFO | 9 | 139681758739344 | decorators.py:78 | send_data_to_fm took 0.099 seconds
2023-12-20 15:18:58	
2023-12-20 08:18:58 | INFO | 9 | 139681758739344 | decorators.py:78 | send_data_to_fm took 0.099 seconds
2023-12-20 15:18:46	
2023-12-20 08:18:46 | INFO | 10 | 140116180990864 | decorators.py:78 | send_data_to_fm took 0.195 seconds
2023-12-20 15:18:46	
2023-12-20 08:18:46 | INFO | 10 | 140116199561552 | decorators.py:78 | send_data_to_fm took 0.213 seconds
2023-12-20 15:18:45	
2023-12-20 08:18:45 | INFO | 9 | 140116199573840 | decorators.py:78 | send_data_to_fm took 0.303 seconds
2023-12-20 15:18:42	
2023-12-20 08:18:42 | INFO | 10 | 139681706883408 | decorators.py:78 | send_data_to_fm took 0.192 seconds
2023-12-20 15:18:40	
2023-12-20 08:18:40 | INFO | 10 | 140116180990864 | decorators.py:78 | send_data_to_fm took 0.191 seconds
2023-12-20 15:18:39	
2023-12-20 08:18:39 | INFO | 10 | 139681706883408 | decorators.py:78 | send_data_to_fm took 0.101 seconds
2023-12-20 15:18:27	
2023-12-20 08:18:27 | INFO | 9 | 139681706912656 | decorators.py:78 | send_data_to_fm took 0.099 seconds
2023-12-20 15:18:25	
2023-12-20 08:18:25 | INFO | 10 | 140116180990576 | decorators.py:78 | send_data_to_fm took 0.094 seconds
2023-12-20 15:18:19	
2023-12-20 08:18:19 | INFO | 10 | 140116180990576 | decorators.py:78 | send_data_to_fm took 0.097 seconds
2023-12-20 15:18:13	
2023-12-20 08:18:13 | INFO | 9 | 139681706912656 | decorators.py:78 | send_data_to_fm took 0.094 seconds
2023-12-20 15:18:08	
2023-12-20 08:18:08 | INFO | 9 | 140116199573840 | decorators.py:78 | send_data_to_fm took 0.018 seconds
2023-12-20 15:18:08	
2023-12-20 08:18:08 | INFO | 9 | 139681758739344 | decorators.py:78 | send_data_to_fm took 0.186 seconds
2023-12-20 15:18:07	
2023-12-20 08:18:07 | INFO | 9 | 139681758739344 | decorators.py:78 | send_data_to_fm took 0.015 seconds
2023-12-20 15:18:05	
2023-12-20 08:18:05 | INFO | 9 | 140116199573840 | decorators.py:78 | send_data_to_fm took 0.099 seconds
2023-12-20 15:17:59	
2023-12-20 08:17:59 | INFO | 10 | 139681706883408 | decorators.py:78 | send_data_to_fm took 0.189 seconds
2023-12-20 15:17:58	
2023-12-20 08:17:58 | INFO | 10 | 140116180990576 | decorators.py:78 | send_data_to_fm took 0.099 seconds
2023-12-20 15:17:56	
2023-12-20 08:17:56 | INFO | 10 | 139681706883408 | decorators.py:78 | send_data_to_fm took 0.096 seconds
2023-12-20 15:17:53	
2023-12-20 08:17:53 | INFO | 9 | 139681758739344 | decorators.py:78 | send_data_to_fm took 0.092 seconds
2023-12-20 15:17:48	
2023-12-20 08:17:48 | INFO | 9 | 139681706912656 | decorators.py:78 | send_data_to_fm took 0.098 seconds
2023-12-20 15:17:47	
2023-12-20 08:17:47 | INFO | 9 | 139681706912656 | decorators.py:78 | send_data_to_fm took 0.100 seconds
2023-12-20 15:17:46	
2023-12-20 08:17:46 | INFO | 9 | 140116199573840 | decorators.py:78 | send_data_to_fm took 0.103 seconds
2023-12-20 15:17:45	
2023-12-20 08:17:45 | INFO | 9 | 139681706912656 | decorators.py:78 | send_data_to_fm took 0.100 seconds
2023-12-20 15:17:45	
2023-12-20 08:17:45 | INFO | 9 | 140116199573840 | decorators.py:78 | send_data_to_fm took 0.108 seconds
2023-12-20 15:17:36	
2023-12-20 08:17:36 | INFO | 10 | 139681706883408 | decorators.py:78 | send_data_to_fm took 0.101 seconds
2023-12-20 15:17:35	
2023-12-20 08:17:35 | INFO | 10 | 140116199561552 | decorators.py:78 | send_data_to_fm took 0.196 seconds
2023-12-20 15:17:22	
2023-12-20 08:17:22 | INFO | 10 | 139681758751344 | decorators.py:78 | send_data_to_fm took 0.103 seconds
2023-12-20 15:17:02	
2023-12-20 08:17:02 | INFO | 10 | 140116180991728 | decorators.py:78 | send_data_to_fm took 0.104 seconds
2023-12-20 15:16:58	
2023-12-20 08:16:58 | INFO | 9 | 139681758739344 | decorators.py:78 | send_data_to_fm took 0.096 seconds
2023-12-20 15:16:56	
2023-12-20 08:16:56 | INFO | 9 | 140116199573840 | decorators.py:78 | send_data_to_fm took 0.112 seconds
2023-12-20 15:16:51	
2023-12-20 08:16:51 | INFO | 9 | 139681462718832 | decorators.py:78 | send_data_to_fm took 0.185 seconds
2023-12-20 15:16:43	
2023-12-20 08:16:43 | INFO | 10 | 140116199561552 | decorators.py:78 | send_data_to_fm took 0.200 seconds
2023-12-20 15:16:36	
2023-12-20 08:16:36 | INFO | 9 | 139681706912656 | decorators.py:78 | send_data_to_fm took 0.099 seconds
2023-12-20 15:16:36	
2023-12-20 08:16:36 | INFO | 9 | 140116199573840 | decorators.py:78 | send_data_to_fm took 0.189 seconds
2023-12-20 15:16:33	
2023-12-20 08:16:33 | INFO | 10 | 140116199561552 | decorators.py:78 | send_data_to_fm took 0.099 seconds
2023-12-20 15:16:31	
2023-12-20 08:16:31 | INFO | 10 | 139681758751344 | decorators.py:78 | send_data_to_fm took 0.188 seconds
2023-12-20 15:16:31	
2023-12-20 08:16:31 | INFO | 10 | 139681758751344 | decorators.py:78 | send_data_to_fm took 0.103 seconds
2023-12-20 15:16:24	
2023-12-20 08:16:24 | INFO | 9 | 140116199573840 | decorators.py:78 | send_data_to_fm took 0.097 seconds
2023-12-20 15:16:23	
2023-12-20 08:16:23 | INFO | 9 | 140116199573840 | decorators.py:78 | send_data_to_fm took 0.100 seconds
2023-12-20 15:16:21	
2023-12-20 08:16:21 | INFO | 10 | 139681758751920 | decorators.py:78 | send_data_to_fm took 0.101 seconds
2023-12-20 15:16:11	
2023-12-20 08:16:11 | INFO | 10 | 139681758751920 | decorators.py:78 | send_data_to_fm took 0.101 seconds
2023-12-20 15:16:04	
2023-12-20 08:16:04 | INFO | 9 | 139681758739344 | decorators.py:78 | send_data_to_fm took 0.102 seconds
2023-12-20 15:16:03	
2023-12-20 08:16:03 | INFO | 9 | 139681758739344 | decorators.py:78 | send_data_to_fm took 0.098 seconds
2023-12-20 15:16:01	
2023-12-20 08:16:01 | INFO | 10 | 140116180991728 | decorators.py:78 | send_data_to_fm took 0.107 seconds
2023-12-20 15:15:42	
2023-12-20 08:15:42 | INFO | 10 | 140116199561552 | decorators.py:78 | send_data_to_fm took 0.191 seconds
2023-12-20 15:15:27	
2023-12-20 08:15:27 | INFO | 9 | 139681706912656 | decorators.py:78 | send_data_to_fm took 0.102 seconds
2023-12-20 15:15:25	
2023-12-20 08:15:25 | INFO | 10 | 140116180990576 | decorators.py:78 | send_data_to_fm took 0.102 seconds
2023-12-20 15:15:24	
2023-12-20 08:15:24 | INFO | 9 | 139681706912656 | decorators.py:78 | send_data_to_fm took 0.100 seconds
2023-12-20 15:15:23	
2023-12-20 08:15:23 | INFO | 9 | 139681706912656 | decorators.py:78 | send_data_to_fm took 0.098 seconds
2023-12-20 15:15:22	
2023-12-20 08:15:22 | INFO | 9 | 139681706912656 | decorators.py:78 | send_data_to_fm took 0.194 seconds
2023-12-20 15:15:21	
2023-12-20 08:15:21 | INFO | 9 | 140116199573840 | decorators.py:78 | send_data_to_fm took 0.106 seconds
2023-12-20 15:15:20	
2023-12-20 08:15:20 | INFO | 9 | 139681706912656 | decorators.py:78 | send_data_to_fm took 0.097 seconds
2023-12-20 15:15:07	
2023-12-20 08:15:07 | INFO | 9 | 139681706912656 | decorators.py:78 | send_data_to_fm took 0.102 seconds
2023-12-20 15:15:04	
2023-12-20 08:15:04 | INFO | 9 | 139681706912656 | decorators.py:78 | send_data_to_fm took 0.184 seconds
2023-12-20 15:15:02	
2023-12-20 08:15:02 | INFO | 10 | 139681758751920 | decorators.py:78 | send_data_to_fm took 0.184 seconds
2023-12-20 15:15:02	
2023-12-20 08:15:02 | INFO | 10 | 140116180990576 | decorators.py:78 | send_data_to_fm took 0.102 seconds
2023-12-20 15:15:01	
2023-12-20 08:15:01 | INFO | 9 | 140116199573840 | decorators.py:78 | send_data_to_fm took 0.202 seconds
2023-12-20 15:15:00	
2023-12-20 08:15:00 | INFO | 9 | 139681706912656 | decorators.py:78 | send_data_to_fm took 0.111 seconds
2023-12-20 15:14:49	
2023-12-20 08:14:49 | INFO | 9 | 139681706912656 | decorators.py:78 | send_data_to_fm took 0.098 seconds
2023-12-20 15:14:48	
2023-12-20 08:14:48 | INFO | 10 | 140116199561552 | decorators.py:78 | send_data_to_fm took 0.186 seconds
2023-12-20 15:14:44	
2023-12-20 08:14:44 | INFO | 10 | 140116199561552 | decorators.py:78 | send_data_to_fm took 0.189 seconds
2023-12-20 15:14:41	
2023-12-20 08:14:41 | INFO | 9 | 139681758739344 | decorators.py:78 | send_data_to_fm took 0.095 seconds
2023-12-20 15:14:40	
2023-12-20 08:14:40 | INFO | 10 | 139681706883408 | decorators.py:78 | send_data_to_fm took 0.203 seconds
2023-12-20 15:14:40	
2023-12-20 08:14:40 | INFO | 9 | 140116199573840 | decorators.py:78 | send_data_to_fm took 0.018 seconds
2023-12-20 15:14:33	
2023-12-20 08:14:33 | INFO | 9 | 140116199573840 | decorators.py:78 | send_data_to_fm took 0.102 seconds
2023-12-20 15:14:29	
2023-12-20 08:14:29 | INFO | 9 | 139681758739344 | decorators.py:78 | send_data_to_fm took 0.099 seconds
2023-12-20 15:14:28	
2023-12-20 08:14:28 | INFO | 9 | 140116199573840 | decorators.py:78 | send_data_to_fm took 0.096 seconds
2023-12-20 15:14:20	
2023-12-20 08:14:20 | INFO | 10 | 139681758751920 | decorators.py:78 | send_data_to_fm took 0.197 seconds
2023-12-20 15:14:13	
2023-12-20 08:14:13 | INFO | 10 | 140116180991440 | decorators.py:78 | send_data_to_fm took 0.105 seconds
2023-12-20 15:14:11	
2023-12-20 08:14:11 | INFO | 9 | 139681706912656 | decorators.py:78 | send_data_to_fm took 0.185 seconds
2023-12-20 15:14:10	
2023-12-20 08:14:10 | INFO | 9 | 139681706912656 | decorators.py:78 | send_data_to_fm took 0.097 seconds
2023-12-20 15:14:07	
2023-12-20 08:14:07 | INFO | 9 | 139681706912656 | decorators.py:78 | send_data_to_fm took 0.102 seconds
2023-12-20 15:14:05	
2023-12-20 08:14:05 | INFO | 9 | 140116199573840 | decorators.py:78 | send_data_to_fm took 0.185 seconds
2023-12-20 15:13:51	
2023-12-20 08:13:51 | INFO | 9 | 140116164270704 | decorators.py:78 | send_data_to_fm took 0.099 seconds
2023-12-20 15:13:50	
2023-12-20 08:13:50 | INFO | 9 | 139681706912656 | decorators.py:78 | send_data_to_fm took 0.111 seconds
2023-12-20 15:13:47	
2023-12-20 08:13:47 | INFO | 10 | 139681706883408 | decorators.py:78 | send_data_to_fm took 0.205 seconds
2023-12-20 15:13:45	
2023-12-20 08:13:45 | INFO | 9 | 140116164270704 | decorators.py:78 | send_data_to_fm took 0.190 seconds
2023-12-20 15:13:45	
2023-12-20 08:13:45 | INFO | 10 | 140116199561552 | decorators.py:78 | send_data_to_fm took 0.185 seconds
2023-12-20 15:13:44	
2023-12-20 08:13:44 | INFO | 10 | 139681706883408 | decorators.py:78 | send_data_to_fm took 0.100 seconds
2023-12-20 15:13:39	
2023-12-20 08:13:39 | INFO | 10 | 140116180991440 | decorators.py:78 | send_data_to_fm took 0.185 seconds
2023-12-20 15:13:35	
2023-12-20 08:13:35 | INFO | 10 | 139681706883408 | decorators.py:78 | send_data_to_fm took 0.100 seconds
2023-12-20 15:13:30	
2023-12-20 08:13:30 | INFO | 9 | 140116164271568 | decorators.py:78 | send_data_to_fm took 0.101 seconds
2023-12-20 15:13:30	
2023-12-20 08:13:30 | INFO | 9 | 139681706912656 | decorators.py:78 | send_data_to_fm took 0.098 seconds
2023-12-20 15:13:25	
2023-12-20 08:13:25 | INFO | 9 | 139681706912656 | decorators.py:78 | send_data_to_fm took 0.021 seconds
2023-12-20 15:13:24	
2023-12-20 08:13:24 | INFO | 9 | 139681706912656 | decorators.py:78 | send_data_to_fm took 0.099 seconds
2023-12-20 15:13:24	
2023-12-20 08:13:24 | INFO | 10 | 140116199561552 | decorators.py:78 | send_data_to_fm took 0.187 seconds
2023-12-20 15:13:21	
2023-12-20 08:13:21 | INFO | 9 | 139681706912656 | decorators.py:78 | send_data_to_fm took 0.100 seconds
2023-12-20 15:13:19	
2023-12-20 08:13:19 | INFO | 9 | 139681706912656 | decorators.py:78 | send_data_to_fm took 0.099 seconds
2023-12-20 15:13:17	
2023-12-20 08:13:17 | INFO | 10 | 140116199561552 | decorators.py:78 | send_data_to_fm took 0.104 seconds
2023-12-20 15:13:15	
2023-12-20 08:13:15 | INFO | 9 | 140116164270704 | decorators.py:78 | send_data_to_fm took 0.094 seconds
2023-12-20 15:13:10	
2023-12-20 08:13:10 | INFO | 10 | 139681706883408 | decorators.py:78 | send_data_to_fm took 0.099 seconds
2023-12-20 15:13:06	
2023-12-20 08:13:06 | INFO | 9 | 139681706912656 | decorators.py:78 | send_data_to_fm took 0.098 seconds
2023-12-20 15:13:05	
2023-12-20 08:13:05 | INFO | 10 | 140116199561552 | decorators.py:78 | send_data_to_fm took 0.019 seconds
2023-12-20 15:13:02	
2023-12-20 08:13:02 | INFO | 10 | 139681758751920 | decorators.py:78 | send_data_to_fm took 0.101 seconds
2023-12-20 15:12:52	
2023-12-20 08:12:52 | INFO | 10 | 140116199561552 | decorators.py:78 | send_data_to_fm took 0.101 seconds
2023-12-20 15:12:49	
2023-12-20 08:12:49 | INFO | 9 | 140116164270704 | decorators.py:78 | send_data_to_fm took 0.104 seconds
2023-12-20 15:12:46	
2023-12-20 08:12:46 | INFO | 9 | 140116199573840 | decorators.py:78 | send_data_to_fm took 0.181 seconds
2023-12-20 15:12:43	
2023-12-20 08:12:43 | INFO | 9 | 140116199573840 | decorators.py:78 | send_data_to_fm took 0.101 seconds
2023-12-20 15:12:42	
2023-12-20 08:12:42 | INFO | 9 | 140116199573840 | decorators.py:78 | send_data_to_fm took 0.188 seconds
2023-12-20 15:12:40	
2023-12-20 08:12:40 | INFO | 9 | 140116199573840 | decorators.py:78 | send_data_to_fm took 0.100 seconds
2023-12-20 15:12:37	
2023-12-20 08:12:37 | INFO | 9 | 140116199573840 | decorators.py:78 | send_data_to_fm took 0.105 seconds
2023-12-20 15:12:36	
2023-12-20 08:12:36 | INFO | 10 | 139681706883408 | decorators.py:78 | send_data_to_fm took 0.204 seconds
2023-12-20 15:12:36	
2023-12-20 08:12:36 | INFO | 9 | 139681706912656 | decorators.py:78 | send_data_to_fm took 0.204 seconds
2023-12-20 15:12:29	
2023-12-20 08:12:29 | INFO | 9 | 139681758739056 | decorators.py:78 | send_data_to_fm took 0.096 seconds
2023-12-20 15:12:21	
2023-12-20 08:12:21 | INFO | 10 | 140116180991728 | decorators.py:78 | send_data_to_fm took 0.184 seconds
2023-12-20 15:12:20	
2023-12-20 08:12:20 | INFO | 10 | 140116180991728 | decorators.py:78 | send_data_to_fm took 0.102 seconds
"""

# Extract durations using regex
durations = re.findall(r'took (\d+\.\d+) seconds', logs)
res = [eval(i) for i in durations]
# Print the extracted durations
for i in res:
    print(i)