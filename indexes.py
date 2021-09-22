'''Ibovespa Indexes'''

# Broad Indexes
BROAD = 'Broad', 'broad', {
    'IBOV': 'Bovespa Index (Ibovespa)',
    'IBXX': 'Brazil 100 Index (IBrX 100)',
    'IBXL': 'Brazil 50 Index (IBrX 50)',
    'IBRA': 'Brazil Broad-Based Index (IBrA)'
}
# Sustainability Indices
SUSTN = 'Sustainability', 'sustn', {
    'ICO2': 'Carbon Efficient Index (ICO2 B3)',
    'ISEE': 'Corporate Sustainability Index (ISE B3)'
}
# Corporate Governance Indices
GOV = 'Corporate Governance', 'gov', {
    'IGCT': 'Corporate Governance Trade Index (IGCT)',
    'IGNM': 'Novo Mercado Corporate Governance Equity Index (IGC-NM)',
    'IGCX': 'Special Corporate Governance Stock Index (IGC)',
    'ITAG': 'Special Tag-Along Stock Index (ITAG)'
}
# Indices for Segments and Sectors
SEGMENT = 'Segments and Sectors', 'segment', {
    'IMAT': 'BM&FBOVESPA Basic Materials Index (IMAT)',
    'ICON': 'BM&FBOVESPA Consumer Stock Index (ICON)',
    'IDIV': 'BM&FBOVESPA Dividend Index (IDIV)',
    'IEEX': 'BM&FBOVESPA Electric Utilities Index (IEE)',
    'IFNC': 'BM&FBOVESPA Financials Index (IFNC)',
    'INDX': 'BM&FBOVESPA Industrials Index (INDX)',
    'UTIL': 'BM&FBOVESPA Public Utilities Index (UTIL)',
    'IMOB': 'BM&FBOVESPA Real Estate Index (IMOB)',
    'IFIL': 'High Liquidity Real Estate Investment Fund Index (IFIX L B3)',
    'MLCX': 'MidLargeCap Index (MLCX)',
    'IFIX': 'Real Estate Investment Fund Index (IFIX)',
    'SMLL': 'SmallCap Index (SMLL)',
    'BDRX': 'Unsponsored BDR Index-GLOBAL (BDRX)',
    'IVBX': 'Valor BM&FBOVESPA Index (IVBX 2)'
}

INDEXES = [SEGMENT, GOV, BROAD, SUSTN]
