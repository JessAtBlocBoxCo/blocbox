                                   Table "public.south_migrationhistory"
  Column   |           Type           |                              Modifiers                              
-----------+--------------------------+---------------------------------------------------------------------
 id        | integer                  | not null default nextval('south_migrationhistory_id_seq'::regclass)
 app_name  | character varying(255)   | not null
 migration | character varying(255)   | not null
 applied   | timestamp with time zone | not null
Indexes:
    "south_migrationhistory_pkey" PRIMARY KEY, btree (id)

