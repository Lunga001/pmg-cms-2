import sqlalchemy
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

engine = create_engine('sqlite:///instance/tmp_drupal.db')

Base = declarative_base()


def __content_type_repr__(self):
    return "<Content_type(pk='%s')>" % self.pk


def get_content_type_model(model_name, fields, model=Base):
    """
    Meta-class for generating database model classes.
    Creates models on the fly, using the builtin 'type' metaclass, see
    http://stackoverflow.com/questions/100003/what-is-a-metaclass-in-python
    """

    field_defs = {
        '__tablename__': model_name.lower(),
        '__repr__': __content_type_repr__,
        'pk': Column(Integer, primary_key=True),
        }

    for field in fields:
        field_defs[field] = Column(String)

    tmp = type(model_name, (model,), field_defs)

    # create the database table if necessary
    Base.metadata.create_all(engine)
    return tmp


def generate_models():

    model_defs = [
        ('audio', [u'start_date', u'title', u'files', u'terms', u'audio', u'revisions', u'_id', u'content_type', u'nid', u'recording_date', u'vid']),
        ('bill', [u'start_date', u'title', u'files', u'terms', u'audio', u'version', u'revisions', u'_id', u'bill_tracker_link_attributes', u'bill_tracker_link_title', u'bill_tracker_link_url', u'content_type', u'delta', u'effective_date', u'file_bill_data', u'file_bill_description', u'file_bill_fid', u'file_bill_list', u'nid', u'vid']),
        ('billsstatus', [u'start_date', u'title', u'files', u'terms', u'audio', u'revisions', u'_id', u'content_type', u'nid', u'vid']),
        ('book', [u'start_date', u'title', u'files', u'terms', u'audio', u'revisions', u'_id', u'content_type', u'embedded_pdf_data', u'embedded_pdf_fid', u'embedded_pdf_list', u'nid', u'vid']),
        ('briefing', [u'start_date', u'title', u'minutes', u'files', u'terms', u'audio', u'revisions', u'_id', u'audio_reference_nid', u'briefing_date', u'content_type', u'delta', u'document_other', u'document_other_format', u'minutes_format', u'nid', u'presentation', u'presentation_format', u'summary', u'summary_format', u'tagline', u'vid']),
        ('calls_comment_public_hearings', [u'start_date', u'title', u'files', u'terms', u'audio', u'revisions', u'_id', u'comment_exp', u'comment_exp2', u'comment_type', u'content_type', u'nid', u'vid']),
        ('comm_info_page', [u'start_date', u'title', u'files', u'terms', u'audio', u'revisions', u'_id', u'comm_info_type', u'content_type', u'nid', u'vid']),
        ('comm_programme', [u'start_date', u'title', u'files', u'terms', u'audio', u'revisions', u'_id', u'comm_programme_data', u'comm_programme_fid', u'comm_programme_list', u'content_type', u'delta', u'embedded_pdf_data', u'embedded_pdf_fid', u'embedded_pdf_list', u'nid', u'vid']),
        ('committee_member', [u'start_date', u'title', u'files', u'terms', u'audio', u'revisions', u'_id', u'commem_img_data', u'commem_img_fid', u'commem_img_list', u'content_type', u'delta', u'mp_adhoc_altmem', u'mp_adhoc_chair', u'mp_adhoc_mem', u'mp_altmember', u'mp_chairperson', u'mp_email_email', u'mp_joint_altmem', u'mp_joint_chair', u'mp_joint_mem', u'mp_link_attributes', u'mp_link_title', u'mp_link_url', u'mp_member', u'mp_ncop_altmem', u'mp_ncop_chair', u'mp_ncop_mem', u'mp_party', u'mp_province', u'nid', u'vid']),
        ('daily_schedule', [u'start_date', u'title', u'files', u'terms', u'audio', u'revisions', u'_id', u'content_type', u'daily_sched_date', u'embedded_pdf_data', u'embedded_pdf_fid', u'embedded_pdf_list', u'nid', u'vid']),
        ('faq', [u'start_date', u'title', u'files', u'terms', u'audio', u'revisions', u'_id', u'content_type', u'nid', u'vid']),
        ('gazette', [u'start_date', u'title', u'files', u'terms', u'audio', u'revisions', u'_id', u'content_type', u'effective_date', u'file_gazette_data', u'file_gazette_description', u'file_gazette_fid', u'file_gazette_list', u'nid', u'vid']),
        ('hansard', [u'start_date', u'title', u'files', u'meeting_date', u'terms', u'audio', u'revisions', u'_id', u'content_type', u'nid', u'vid']),
        ('home_image', [u'start_date', u'title', u'files', u'terms', u'audio', u'revisions', u'_id', u'content_type', u'home_image_data', u'home_image_fid', u'home_image_list', u'homeimg_link', u'nid', u'vid']),
        ('mp_blog', [u'start_date', u'title', u'files', u'terms', u'audio', u'revisions', u'_id', u'content_type', u'nid', u'vid']),
        ('newsletter', [u'start_date', u'title', u'files', u'terms', u'audio', u'revisions', u'_id', u'content_type', u'delta', u'embedded_pdf_data', u'embedded_pdf_fid', u'embedded_pdf_list', u'newsletter_edition', u'newsletter_edition_month', u'newsletter_headline', u'newsletter_image_data', u'newsletter_image_fid', u'newsletter_image_list', u'newsletter_lead', u'newsletter_lead_format', u'newsletter_type', u'nid', u'vid']),
        ('page', [u'start_date', u'title', u'files', u'terms', u'audio', u'revisions', u'_id', u'content_type', u'nid', u'vid']),
        ('policy_document', [u'start_date', u'title', u'files', u'terms', u'audio', u'revisions', u'_id', u'content_type', u'effective_date', u'file_policy_doc_data', u'file_policy_doc_description', u'file_policy_doc_fid', u'file_policy_doc_list', u'nid', u'vid']),
        ('programme', [u'start_date', u'title', u'files', u'terms', u'audio', u'revisions', u'_id', u'content_type', u'nid', u'vid']),
        ('questions_replies', [u'start_date', u'title', u'files', u'terms', u'audio', u'revisions', u'_id', u'content_type', u'nid', u'question_number', u'vid']),
        ('report', [u'start_date', u'title', u'minutes', u'files', u'meeting_date', u'terms', u'audio', u'revisions', u'_id', u'chairperson', u'content_type', u'minutes_format', u'nid', u'vid']),
        ('tabled_committee_reports', [u'start_date', u'title', u'files', u'terms', u'audio', u'revisions', u'_id', u'content_type', u'nid', u'vid']),
        ]

    model_dict = {}

    for name, fields in model_defs:
        model_dict[name] = get_content_type_model(name, fields)

    return model_dict


if __name__ == "__main__":

    model_name = 'bill'
    fields = [u'files', u'audio', u'terms', u'vid', u'title', u'file_bill_fid', u'file_bill_list', u'nid', u'bill_tracker_link_attributes', u'file_bill_description', u'version', u'bill_tracker_link_title', u'content_type', u'delta', u'effective_date', u'file_bill_data', u'_id', u'start_date', u'bill_tracker_link_url', u'revisions']

    model = get_content_type_model(model_name, fields)
