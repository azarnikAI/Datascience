import pandas as pd

def dataframe_to_html(df, columns):
    #tdstyle="style='word-wrap: break-word;min-width: 260px;max-width: 160px;'"
    tdstyle=""
    html=["""<html><head>  
    <title>Bootstrap Example</title>  
    <meta charset="utf-8">  
    <meta name="viewport" content="width=device-width, initial-scale=1">  
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta.2/css/bootstrap.min.css">  
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>  
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.6/umd/popper.min.js"></script>  
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta.2/js/bootstrap.min.js"></script>  
    <style>
    .table-striped tbody tr:nth-child(odd) {
    background-color: #DAE9EB; /* color for odd rows */
    }

    .table-striped tbody tr:nth-child(even) {
    background-color: #9ADC9F; /* color for even rows */
    }
    </style>
    </head>  

    <body>
    <div class="table-responsive">
    <table class="table table-striped table-bordered"  ><tr><td>No</td>"""]
    for i in columns:
        html.append(f'<td>{i}</td>')
    
    html.append("</tr>")   
    i=1
    for index, row in df.iterrows():
        rd=[f"<tr><td>{i}</td>"]
        for c in columns:
            rd.append(f"<td {tdstyle}>{row[c]}</td>")
        rd.append("</tr>")
        html.append(''.join(rd))
        i+=1    
    html.append("</table></div></body></html>")
    return ''.join(html)
#######################################################
sheet_name = 'sheetname'


columns = ['col1','col2']#determine columns



# Read the Excel file
df = pd.read_excel('papers_Ai_new.xlsx', sheet_name=sheet_name, usecols=columns)
htm= dataframe_to_html(df , columns)
with open('result.html', 'w', encoding='utf8') as file2:

    # write contents to the test2.txt file
    file2.write(htm)