select
    "User Id"                              as user_id,
    "Full Name"                            as full_name,
    lower("Sex")                           as sex,
    lower("Email")                         as email,
    "Phone"                                as phone,
    "Age"                                  as age,
    "Job Title"                            as job_title
from {{ source('raw', 'users') }}
