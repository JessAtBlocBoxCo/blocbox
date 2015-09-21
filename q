                                Table "public.calendar_homebrew_hostconflicts_dateversion"
       Column        |  Type   |                                        Modifiers                                         
---------------------+---------+------------------------------------------------------------------------------------------
 id                  | integer | not null default nextval('calendar_homebrew_hostconflicts_dateversion_id_seq'::regclass)
 thimonthconflict1   | date    | 
 thimonthconflict2   | date    | 
 thimonthconflict3   | date    | 
 thimonthconflict4   | date    | 
 thimonthconflict5   | date    | 
 thimonthconflict6   | date    | 
 thimonthconflict7   | date    | 
 thimonthconflict8   | date    | 
 thimonthconflict9   | date    | 
 thimonthconflict10  | date    | 
 thimonthconflict11  | date    | 
 thimonthconflict12  | date    | 
 thimonthconflict13  | date    | 
 thimonthconflict14  | date    | 
 thimonthconflict15  | date    | 
 thimonthconflict16  | date    | 
 thimonthconflict17  | date    | 
 thimonthconflict18  | date    | 
 thimonthconflict19  | date    | 
 thimonthconflict20  | date    | 
 thimonthconflict21  | date    | 
 thimonthconflict22  | date    | 
 thimonthconflict23  | date    | 
 thimonthconflict24  | date    | 
 thimonthconflict25  | date    | 
 thimonthconflict26  | date    | 
 thimonthconflict27  | date    | 
 thimonthconflict28  | date    | 
 thimonthconflict29  | date    | 
 thimonthconflict30  | date    | 
 thimonthconflict31  | date    | 
 nextmonthconflict1  | date    | 
 nextmonthconflict2  | date    | 
 nextmonthconflict3  | date    | 
 nextmonthconflict4  | date    | 
 nextmonthconflict5  | date    | 
 nextmonthconflict6  | date    | 
 nextmonthconflict7  | date    | 
 nextmonthconflict8  | date    | 
 nextmonthconflict9  | date    | 
 nextmonthconflict10 | date    | 
 nextmonthconflict11 | date    | 
 nextmonthconflict12 | date    | 
 nextmonthconflict13 | date    | 
 nextmonthconflict14 | date    | 
 nextmonthconflict15 | date    | 
 nextmonthconflict16 | date    | 
 nextmonthconflict17 | date    | 
 nextmonthconflict18 | date    | 
 nextmonthconflict19 | date    | 
 nextmonthconflict20 | date    | 
 nextmonthconflict21 | date    | 
 nextmonthconflict22 | date    | 
 nextmonthconflict23 | date    | 
 nextmonthconflict24 | date    | 
 nextmonthconflict25 | date    | 
 nextmonthconflict26 | date    | 
 nextmonthconflict27 | date    | 
 nextmonthconflict28 | date    | 
 nextmonthconflict29 | date    | 
 nextmonthconflict30 | date    | 
 nextmonthconflict31 | date    | 
 host_id             | integer | not null
Indexes:
    "calendar_homebrew_hostconflicts_dateversion_pkey" PRIMARY KEY, btree (id)
    "calendar_homebrew_hostconflicts_dateversion_8396f175" btree (host_id)
Foreign-key constraints:
    "calendar_homebrew_h_host_id_88273a2e965a5c0_fk_core_userinfo_id" FOREIGN KEY (host_id) REFERENCES core_userinfo(id) DEFERRABLE INITIALLY DEFERRED

