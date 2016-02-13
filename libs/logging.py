import traceback, smtplib
from datetime import datetime
from config.security import E500_EMAIL_ADDRESS, SYSADMIN_EMAILS

def log_and_email_error(e, message=None, emails=SYSADMIN_EMAILS ):
    """ Prints in the server logs (defaults to Apache if not specified),
        does NOT stop execution. """
    try:
        error_email = 'Subject: %s\n\n%s' % ("Beiwe 500 Error",
                                             log_error(e, message, reraise=True) )
        email_server = smtplib.SMTP("localhost")
        email_server.sendmail( E500_EMAIL_ADDRESS, emails, error_email )
        email_server.quit()
    except Exception:
        print("\n!!!! ERROR IN log_and_email_error !!!!")


def log_error(e, message=None, reraise=False):
    """ Prints an error to the apache log.
        Reraise is dangerous, only set to true if you understand why it is."""
    try:
        error_message = "===================\n"
        error_message += datetime.utcnow().isoformat() + "\n"
        if message is not None: error_message += message + "\n"
        error_message += "ERROR:\n" + str(e.__repr__()) + "\n"
        error_message += traceback.format_exc() + "\n"
        error_message += "===================\n"
        print(error_message)
        return error_message
    except Exception:
        print("\n!!!! ERROR IN log_error !!!!")
        if reraise:
            raise