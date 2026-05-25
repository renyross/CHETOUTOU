import bs4

def build_harnais():
    with open('produit-impermeable.html', 'r', encoding='utf-8') as f:
        template_soup = bs4.BeautifulSoup(f, 'html.parser')
        
    with open('harnais-confort-anti-traction.html', 'r', encoding='utf-8') as f:
        data_soup = bs4.BeautifulSoup(f, 'html.parser')

    # 1. Update Title and Meta
    template_soup.title.string = data_soup.title.string
    meta_desc_template = template_soup.find('meta', {'name': 'description'})
    meta_desc_data = data_soup.find('meta', {'name': 'description'})
    if meta_desc_template and meta_desc_data:
        meta_desc_template['content'] = meta_desc_data['content']

    # 2. Update Breadcrumb
    template_breadcrumb = template_soup.find('nav', class_='breadcrumb')
    data_breadcrumb = data_soup.find('nav', class_='breadcrumb')
    if template_breadcrumb and data_breadcrumb:
        template_breadcrumb.replace_with(data_breadcrumb)

    # 3. Update Gallery
    template_gallery = template_soup.find('div', class_='product-gallery')
    data_gallery = data_soup.find('div', class_='product-gallery')
    if template_gallery and data_gallery:
        template_gallery.replace_with(data_gallery)

    # 4. Update Product Info
    template_info = template_soup.find('div', class_='product-info-column')
    data_info = data_soup.find('div', class_='product-info-column')
    if template_info and data_info:
        template_info.replace_with(data_info)

    # 5. Update Features Showcase
    template_features = template_soup.find('section', class_='product-features-showcase')
    data_features = data_soup.find('section', class_='product-features-showcase')
    if template_features and data_features:
        template_features.replace_with(data_features)

    # 6. Update Reviews Summary
    template_reviews_summary = template_soup.find('div', class_='reviews-summary-v3')
    data_reviews_summary = data_soup.find('div', class_='reviews-summary-v3')
    if template_reviews_summary and data_reviews_summary:
        template_reviews_summary.replace_with(data_reviews_summary)

    # 7. Add FAQ for Harness
    faq_section = template_soup.find('section', class_='pdp-faq-section')
    if faq_section:
        faq_list = faq_section.find('div', class_='faq-list')
        if faq_list:
            faq_list.clear()
            
            questions = [
                ("Comment bien ajuster le harnais ?", "Pour un ajustement optimal, mesurez le tour de poitrail de votre chien. Le harnais doit être ajusté de façon à pouvoir passer deux doigts entre les sangles et le corps de l'animal. Ajustez d'abord le cou, puis le poitrail."),
                ("Est-il adapté aux chiens qui tirent très fort ?", "Oui, ce harnais a été spécialement conçu pour l'anti-traction. Son attache frontale permet de faire pivoter légèrement le chien vers vous lorsqu'il tire, interrompant naturellement son élan sans aucune compression de la trachée."),
                ("Comment entretenir et laver le harnais ?", "Nous recommandons un lavage à la main à l'eau tiède avec un savon doux. Vous pouvez également le passer en machine à 30°C dans un filet de lavage. Laissez-le sécher à l'air libre, ne le mettez pas au sèche-linge.")
            ]
            
            for q, a in questions:
                faq_item = template_soup.new_tag('div', attrs={'class': 'faq-item'})
                
                btn = template_soup.new_tag('button', attrs={'class': 'faq-question'})
                btn.string = q + " "
                span = template_soup.new_tag('span', attrs={'class': 'faq-icon'})
                span.string = "+"
                btn.append(span)
                
                answer_div = template_soup.new_tag('div', attrs={'class': 'faq-answer'})
                p = template_soup.new_tag('p')
                p.string = a
                answer_div.append(p)
                
                faq_item.append(btn)
                faq_item.append(answer_div)
                
                faq_list.append(faq_item)

    # Update canonical links or any links pointing to harnais-confort-anti-traction
    for a in template_soup.find_all('a', href='harnais-confort-anti-traction.html'):
        a['href'] = 'harnais-anti-traction.html'

    with open('harnais-anti-traction.html', 'w', encoding='utf-8') as f:
        f.write(str(template_soup))
        
    print("Successfully built harnais-anti-traction.html")

if __name__ == '__main__':
    build_harnais()
