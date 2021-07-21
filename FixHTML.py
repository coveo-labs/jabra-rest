#Fix FamilyName in quickview

try:
  #Get Body HTML
  filetype = document.get_meta_data_value("filetype")[0]
  if (filetype=='Pairing Guide'):
    bodytext = document.DataStream('body_html')

    model = document.get_meta_data_value("mymodel")[0]
    # Read the original text
    extracted_text = document.get_data_stream('body_html', 'converter').read().replace('\n', ' ')
    extracted_text = extracted_text.replace('[FamilyName]',model)
    # Write to the bodytext holder
    bodytext.write(extracted_text)

    # Add the datastream back in
    document.add_data_stream(bodytext)
except Exception as e:
    log(str(e))

