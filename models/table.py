# coding: utf8
import datetime
#now = datetime.datetime.now()
def get_emails():
    if auth.user:
        return auth.user.email
    else:
        return ''

    
db.define_table('Static_image',
                Field('id', 'integer'),
                Field('photo', 'upload'),
                )

db.define_table('Anthro_classses',
                Field('id', 'integer'),
                Field('Course_Number', 'string'),
                format='%(Course_Number)s'
)

db.define_table("Sales_Posting_Anthropology",
                Field('Post_date', 'datetime', default=request.now, update=request.now, writable=False),
                Field('Course_title', db.Anthro_classses),
                Field('Book_title', 'string'),
                Field('Price', 'integer'),
                Field('Description', 'text'),
                Field('Contact_email', 'string', default=get_emails(), writable=False),
                Field('Item_Image', 'upload'),
                )

db.define_table('Biochem_classses',
                Field('id', 'integer'),
                Field('Course_Number', 'string'),
                format='%(Course_Number)s'
)

db.define_table("Sales_Posting_Biochemistry_and_Molecular_Bio",
                Field('Post_date', 'datetime', default=request.now, update=request.now, writable=False),
                Field('Course_title', db.Biochem_classses),
                Field('Book_title', 'string'),
                Field('Price', 'integer'),
                Field('Description', 'text'),
                Field('Contact_email', 'string', default=get_emails(), writable=False),
                Field('Item_Image', 'upload')
                )

db.define_table('Bio_classses',
                Field('id', 'integer'),
                Field('Course_Number', 'string'),
                format='%(Course_Number)s'
)

db.define_table("Sales_Posting_Biology",
                Field('Post_date', 'datetime', default=request.now, update=request.now, writable=False),
                Field('Course_title', db.Bio_classses),
                Field('Book_title', 'string'),
                Field('Price', 'integer'),
                Field('Description', 'text'),
                Field('Contact_email', 'string', default=get_emails(), writable=False),
                Field('Item_Image', 'upload')
                )

db.define_table('Chem_classses',
                Field('id', 'integer'),
                Field('Course_Number', 'string'),
                format='%(Course_Number)s'
)

db.define_table("Sales_Posting_Chemistry",
                Field('Post_date', 'datetime', default=request.now, update=request.now, writable=False),
                Field('Course_title', db.Chem_classses),
                Field('Book_title', 'string'),
                Field('Price', 'integer'),
                Field('Description', 'text'),
                Field('Contact_email', 'string', default=get_emails(), writable=False),
                Field('Item_Image', 'upload')
                )

db.define_table('CE_FIX_classses',
                Field('id', 'integer'),
                Field('Course_Number', 'string'),
                format='%(Course_Number)s'
)

db.define_table("Sales_Posting_Computerengineering",
                Field('Post_date', 'datetime', default=request.now, update=request.now, writable=False),
                Field('Course_title', db.Biochem_classses),
                Field('Book_title', 'string'),
                Field('Price', 'integer'),
                Field('Description', 'text'),
                Field('Contact_email', 'string', default=get_emails(), writable=False),
                Field('Item_Image', 'upload')
                )

db.define_table('CS_classses',
                Field('id', 'integer'),
                Field('Course_Number', 'string'),
                format='%(Course_Number)s'
)

db.define_table("Sales_Posting_Computerscience",
                Field('Post_date', 'datetime', default=request.now, update=request.now, writable=False),
                Field('Course_title', db.CS_classses),
                Field('Book_title', 'string'),
                Field('Price', 'integer'),
                Field('Description', 'text'),
                Field('Contact_email', 'string', default=get_emails(), writable=False),
                Field('Item_Image', 'upload')
                )

db.define_table('Earth_classses',
                Field('id', 'integer'),
                Field('Course_Number', 'string'),
                format='%(Course_Number)s'
)

db.define_table("Sales_Posting_Earth_Sciences_and_Ecology",
                Field('Post_date', 'datetime', default=request.now, update=request.now, writable=False),
                Field('Course_title', db.Earth_classses),
                Field('Book_title', 'string'),
                Field('Price', 'integer'),
                Field('Description', 'text'),
                Field('Contact_email', 'string', default=get_emails(), writable=False),
                Field('Item_Image', 'upload')
                )

db.define_table('Econ_classses',
                Field('id', 'integer'),
                Field('Course_Number', 'string'),
                format='%(Course_Number)s'
)

db.define_table("Sales_Posting_Economics",
                Field('Post_date', 'datetime', default=request.now, update=request.now, writable=False),
                Field('Course_title', db.Econ_classses),
                Field('Book_title', 'string'),
                Field('Price', 'integer'),
                Field('Description', 'text'),
                Field('Contact_email', 'string', default=get_emails(), writable=False),
                Field('Item_Image', 'upload')
                )

db.define_table('Edu_classses',
                Field('id', 'integer'),
                Field('Course_Number', 'string'),
                format='%(Course_Number)s'
)

db.define_table("Sales_Posting_Education",
                Field('Post_date', 'datetime', default=request.now, update=request.now, writable=False),
                Field('Course_title', db.Edu_classses),
                Field('Book_title', 'string'),
                Field('Price', 'integer'),
                Field('Description', 'text'),
                Field('Contact_email', 'string', default=get_emails(), writable=False),
                Field('Item_Image', 'upload')
                )

db.define_table('Envs_classses',
                Field('Course_Number', 'string'),
                format='%(Course_Number)s'
)

db.define_table("Sales_Posting_Environmental_Studies",
                Field('Post_date', 'datetime', default=request.now, update=request.now, writable=False),
                Field('Course_title', db.Envs_classses),
                Field('Book_title', 'string'),
                Field('Price', 'integer'),
                Field('Description', 'text'),
                Field('Contact_email', 'string', default=get_emails(), writable=False),
                Field('Item_Image', 'upload')
                )

db.define_table('Film_classses',
                Field('id', 'integer'),
                Field('Course_Number', 'string'),
                format='%(Course_Number)s'
)

db.define_table("Sales_Posting_Film",
                Field('Post_date', 'datetime', default=request.now, update=request.now, writable=False),
                Field('Course_title', db.Film_classses),
                Field('Book_title', 'string'),
                Field('Price', 'integer'),
                Field('Description', 'text'),
                Field('Contact_email', 'string', default=get_emails(), writable=False),
                Field('Item_Image', 'upload')
                )

db.define_table('Hist_classses',
                Field('id', 'integer'),
                Field('Course_Number', 'string'),
                format='%(Course_Number)s'
)

db.define_table("Sales_Posting_History",
                Field('Post_date', 'datetime', default=request.now, update=request.now, writable=False),
                Field('Course_title', db.Hist_classses),
                Field('Book_title', 'string'),
                Field('Price', 'integer'),
                Field('Description', 'text'),
                Field('Contact_email', 'string', default=get_emails(), writable=False),
                Field('Item_Image', 'upload')
                )

db.define_table('Havc_classses',
                Field('id', 'integer'),
                Field('Course_Number', 'string'),
                format='%(Course_Number)s'
)

db.define_table("Sales_Posting_History_and_Visual_Culture",
                Field('Post_date', 'datetime', default=request.now, update=request.now, writable=False),
                Field('Course_title', db.Havc_classses),
                Field('Book_title', 'string'),
                Field('Price', 'integer'),
                Field('Description', 'text'),
                Field('Contact_email', 'string', default=get_emails(), writable=False),
                Field('Item_Image', 'upload')
                )

db.define_table('Ling_classses',
                Field('id', 'integer'),
                Field('Course_Number', 'string'),
                format='%(Course_Number)s'
)

db.define_table("Sales_Posting_Linguistics",
                Field('Post_date', 'datetime', default=request.now, update=request.now, writable=False),
                Field('Course_title', db.Ling_classses),
                Field('Book_title', 'string'),
                Field('Price', 'integer'),
                Field('Description', 'text'),
                Field('Contact_email', 'string', default=get_emails(), writable=False),
                Field('Item_Image', 'upload')
                )

db.define_table('Lit_classses',
                Field('id', 'integer'),
                Field('Course_Number', 'string'),
                format='%(Course_Number)s'
)

db.define_table("Sales_Posting_Literature",
                Field('Post_date', 'datetime', default=request.now, update=request.now, writable=False),
                Field('Course_title', db.Lit_classses),
                Field('Book_title', 'string'),
                Field('Price', 'integer'),
                Field('Description', 'text'),
                Field('Contact_email', 'string', default=get_emails(), writable=False),
                Field('Item_Image', 'upload')
                )

db.define_table('Marine_classses',
                Field('id', 'integer'),
                Field('Course_Number', 'string'),
                format='%(Course_Number)s'
)

db.define_table("Sales_Posting_Marine_Biology",
                Field('Post_date', 'datetime', default=request.now, update=request.now, writable=False),
                Field('Course_title', db.Marine_classses),
                Field('Book_title', 'string'),
                Field('Price', 'integer'),
                Field('Description', 'text'),
                Field('Contact_email', 'string', default=get_emails(), writable=False),
                Field('Item_Image', 'upload')
                )

db.define_table('Math_classses',
                Field('id', 'integer'),
                Field('Course_Number', 'string'),
                format='%(Course_Number)s'
)

db.define_table("Sales_Posting_Mathematics",
                Field('Post_date', 'datetime', default=request.now, update=request.now, writable=False),
                Field('Course_title', db.Math_classses),
                Field('Book_title', 'string'),
                Field('Price', 'integer'),
                Field('Description', 'text'),
                Field('Contact_email', 'string', default=get_emails(), writable=False),
                Field('Item_Image', 'upload')
                )

db.define_table('Music_classses',
                Field('id', 'integer'),
                Field('Course_Number', 'string'),
                format='%(Course_Number)s'
)

db.define_table("Sales_Posting_Music",
                Field('Post_date', 'datetime', default=request.now, update=request.now, writable=False),
                Field('Course_title', db.Music_classses),
                Field('Book_title', 'string'),
                Field('Price', 'integer'),
                Field('Description', 'text'),
                Field('Contact_email', 'string', default=get_emails(), writable=False),
                Field('Item_Image', 'upload')
                )

db.define_table('Phil_classses',
                Field('id', 'integer'),
                Field('Course_Number', 'string'),
                format='%(Course_Number)s'
)

db.define_table("Sales_Posting_Philosophy",
                Field('Post_date', 'datetime', default=request.now, update=request.now, writable=False),
                Field('Course_title', db.Phil_classses),
                Field('Book_title', 'string'),
                Field('Price', 'integer'),
                Field('Description', 'text'),
                Field('Contact_email', 'string', default=get_emails(), writable=False),
                Field('Item_Image', 'upload')
                )

db.define_table('Physics_classses',
                Field('id', 'integer'),
                Field('Course_Number', 'string'),
                format='%(Course_Number)s'
)

db.define_table("Sales_Posting_Physics",
                Field('Post_date', 'datetime', default=request.now, update=request.now, writable=False),
                Field('Course_title', db.Physics_classses),
                Field('Book_title', 'string'),
                Field('Price', 'integer'),
                Field('Description', 'text'),
                Field('Contact_email', 'string', default=get_emails(), writable=False),
                Field('Item_Image', 'upload')
                )

db.define_table('Politics_classses',
                Field('id', 'integer'),
                Field('Course_Number', 'string'),
                format='%(Course_Number)'
)

db.define_table("Sales_Posting_Politics",
                Field('Post_date', 'datetime', default=request.now, update=request.now, writable=False),
                Field('Course_title', db.Politics_classses),
                Field('Book_title', 'string'),
                Field('Price', 'integer'),
                Field('Description', 'text'),
                Field('Contact_email', 'string', default=get_emails(), writable=False),
                Field('Item_Image', 'upload')
                )

db.define_table('Psych_classses',
                Field('id', 'integer'),
                Field('Course_Number', 'string'),
                format='%(Course_Number)s'
)

db.define_table("Sales_Posting_Psychology",
                Field('Post_date', 'datetime', default=request.now, update=request.now, writable=False),
                Field('Course_title', db.Psych_classses),
                Field('Book_title', 'string'),
                Field('Price', 'integer'),
                Field('Description', 'text'),
                Field('Contact_email', 'string', default=get_emails(), writable=False),
                Field('Item_Image', 'upload')
                )

db.define_table('Socio_classses',
                Field('id', 'integer'),
                Field('Course_Number', 'string'),
                format='%(Course_Number)s'
)

db.define_table("Sales_Posting_Sociology",
                Field('Post_date', 'datetime', default=request.now, update=request.now, writable=False),
                Field('Course_title', db.Socio_classses),
                Field('Book_title', 'string'),
                Field('Price', 'integer'),
                Field('Description', 'text'),
                Field('Contact_email', 'string', default=get_emails(), writable=False),
                Field('Item_Image', 'upload')
                )

db.define_table('Tim_classses',
                Field('id', 'integer'),
                Field('Course_Number', 'string'),
                format='%(Course_Number)s'
)

db.define_table("Sales_Posting_Technology_and_Information_Management",
                Field('Post_date', 'datetime', default=request.now, update=request.now, writable=False),
                Field('Course_title', db.Tim_classses),
                Field('Book_title', 'string'),
                Field('Price', 'integer'),
                Field('Description', 'text'),
                Field('Contact_email', 'string', default=get_emails(), writable=False),
                Field('Item_Image', 'upload')
                )

db.define_table('Writing_classses',
                Field('id', 'integer'),
                Field('Course_Number', 'string'),
                format='%(Course_Number)s'
)

db.define_table("Sales_Posting_Writing",
                Field('Post_date', 'datetime', default=request.now, update=request.now, writable=False),
                Field('Course_title', db.Writing_classses),
                Field('Book_title', 'string'),
                Field('Price', 'integer'),
                Field('Description', 'text'),
                Field('Contact_email', 'string', default=get_emails(), writable=False),
                Field('Item_Image', 'upload')
                )

db.define_table("Sales_Posting_Other_and_Misc",
                Field('Post_date', 'datetime', default=request.now, update=request.now, writable=False),
                Field('Item_title', 'string'),
                Field('Price', 'integer'),
                Field('Description', 'text'),
                Field('Contact_email', 'string', default=get_emails(), writable=False),
                Field('Item_Image', 'upload')
                )

db.define_table('Lals_classses',
                Field('id', 'integer'),
                Field('Course_Number', 'string'),
                format='%(Course_Number)s'
)

db.define_table("Sales_Posting_LALS",
                Field('Post_date', 'datetime', default=request.now, update=request.now, writable=False),
                Field('Course_title', db.Lals_classses),
                Field('Book_title', 'string'),
                Field('Price', 'integer'),
                Field('Description', 'text'),
                Field('Contact_email', 'string', default=get_emails(), writable=False),
                Field('Item_Image', 'upload')
                )
