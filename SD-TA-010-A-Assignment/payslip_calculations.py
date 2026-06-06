from decimal import Decimal
from datetime import date, timedelta
from calendar import monthrange

STANDARD_RATE_BAND = Decimal('44000')
PAYE_STANDARD_RATE = Decimal('0.20')
PAYE_HIGHER_RATE = Decimal('0.40')

PERSONAL_TAX_CREDIT = Decimal('1875')
PAYE_TAX_CREDIT = Decimal('1875')
TOTAL_TAX_CREDITS = PERSONAL_TAX_CREDIT + PAYE_TAX_CREDIT

PRSI_EXEMPTION_THRESHOLD = Decimal('18304')
PRSI_RATE = Decimal('0.041')

USC_EXEMPTION_THRESHOLD = Decimal('13000')
USC_BANDS = [('12012', '0.005'), ('27382', '0.02'), ('70044', '0.04'), (float('inf'), '0.08')]


def calculate_paye(annual_salary):
    """
    Calculate PAYE tax

    Args:
        annual_salary(str): Annual salary
    
    Returns:
        Decimal: annual PAYE tax

    """
    salary = Decimal(annual_salary)
    if salary <= STANDARD_RATE_BAND:
        gross_tax = salary * PAYE_STANDARD_RATE
    else:
        gross_tax = (STANDARD_RATE_BAND * PAYE_STANDARD_RATE) + (salary - STANDARD_RATE_BAND) * PAYE_HIGHER_RATE
    
    return max(Decimal('0'), gross_tax - TOTAL_TAX_CREDITS)


def calculate_prsi(annual_salary):
    """
    Calculate PRSI tax

    Args:
        annual_salary(str): Annual salary
    
    Returns:
        Decimal: Annual PRSI tax

    """
    salary = Decimal(annual_salary)
    if salary <= PRSI_EXEMPTION_THRESHOLD:
        return Decimal('0')
    else:
        return salary * PRSI_RATE


def calculate_usc(annual_salary):
    """
    Calculate USC tax

    Args:
        annual_salary(str): Annual salary
    
    Returns:
        Decimal: Annual USC tax

    """
    salary = Decimal(annual_salary)
    if salary <= USC_EXEMPTION_THRESHOLD:
        return Decimal('0')
    
    usc = Decimal('0')
    prev_limit = Decimal('0')

    for band_limit, rate in USC_BANDS:
        if salary <= Decimal(band_limit):
            usc += (salary - prev_limit) * Decimal(rate)
            break
        else:
            usc += (Decimal(band_limit) - prev_limit) * Decimal(rate)
            prev_limit = Decimal(band_limit)
    
    return round(usc, 2)


def calculate_monthly_gross(annual_salary):
    """
    Calculate monthly gross pay

    Args:
        annual_salary(str): Annual salary
    
    Returns:
        Decimal: Monthly gross pay

    """
    return round(Decimal(annual_salary) / Decimal('12'), 2)


def calculate_total_deductions(annual_salary):
    """
    Calculate annual tax deductions

    Args:
        annual_salary(str): Annual salary
    
    Returns:
        Decimal: Annual tax deductions

    """
    paye = calculate_paye(annual_salary)
    prsi = calculate_prsi(annual_salary)
    usc = calculate_usc(annual_salary)
    
    return paye + prsi + usc


def calculate_monthly_net_pay(annual_salary):
    """
    Calculate monthly net pay

    Args:
        annual_salary(str): Annual salary
    
    Returns:
        Decimal: Monthly net pay

    """
    salary = Decimal(annual_salary)
    deductions = calculate_total_deductions(annual_salary)
    annual_net_pay = salary - deductions

    return round(annual_net_pay / Decimal('12'), 2)


def calculate_monthly_deductions(annual_salary):
    """
    Calculate monthly tax deductions

    Args:
        annual_salary(str): Annual salary
    
    Returns:
        Decimal: Monthly tax deductions

    """
    return round(calculate_total_deductions(annual_salary) / Decimal('12'), 2)


def calculate_monthly_prsi(annual_salary):
    """
    Calculate monthly PRSI tax

    Args:
        annual_salary(str): Annual salary
    
    Returns:
        Decimal: Monthly PRSI tax

    """
    return round(calculate_prsi(annual_salary) / Decimal('12'), 2)


def calculate_monthly_paye(annual_salary):
    """
    Calculate monthly PAYE tax

    Args:
        annual_salary(str): Annual salary
    
    Returns:
        Decimal: Monthly PAYE tax

    """
    return round(calculate_paye(annual_salary) / Decimal('12'), 2)


def calculate_monthly_usc(annual_salary):
    """
    Calculate monthly USC tax

    Args:
        annual_salary(str): Annual salary
    
    Returns:
        Decimal: Monthly USC tax

    """
    return round(calculate_usc(annual_salary) / Decimal('12'), 2)

#calculate payment date which is on the last Friday of every pay period
def calculate_payment_date():
    """
    Calculate payment date for the period when a payslip is generated.

    Returns:
        str: The date of last Friday of the payment period in the DD/MM/YY format

    """
    year = date.today().year
    month = date.today().month
    last_day = monthrange(year, month)[1]
    last_date = date(year, month, last_day)
    last_friday = last_date - timedelta((last_date.weekday() - 4) % 7)

    return last_friday.strftime('%d/%m/%y')

def calculate_pay_period():
    """
    Calculate payment period when a payslip is generated.

    Returns:
        str: The date of payment period in the MM/YY format

    """
    return date.today().strftime('%m/%y')
