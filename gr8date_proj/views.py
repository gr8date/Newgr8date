from django.shortcuts import render
from django.contrib import messages

def index(request):
    """Main landing page view."""
    return render(request, 'index.html')

def city_landing(request, city_slug):
    """
    Final Master View: Handles all 8 Cities + all 5 Legal/Support pages.
    """
    # Logic to identify legal pages to hide the 'Join' button in the template
    legal_slugs = ['about', 'privacy', 'terms', 'faq', 'contact']
    is_legal_page = city_slug.lower() in legal_slugs
    
    city_data = {
        'sydney': {
            'name': 'Sydney', 'tag': 'The Harbour Standard', 'hero_folder': 'sydney',
            'meta_title': 'Sydney Dating | Australia’s Premier Free Private Network',
            'h2': 'Refined Elegance in the <span>Harbour City.</span>',
            'text': '''
                <p>Sydney is a city defined by its global stature and its relentless pursuit of excellence. From the glittering shores of Watsons Bay to the corporate pulse of the CBD, dating in Sydney requires a certain level of sophistication and intentionality. The "Harbour Standard" isn't just a catchphrase; it is a lifestyle that demands authenticity and discretion.</p>
                <p>At GR8Date Sydney, we understand that your time is your most valuable asset. That is why we have built a network that mirrors the city’s own standards—refined, transparent, and high-achieving. Whether you are looking for a sunset cocktail at Opera Bar or a quiet, high-end dinner in Surry Hills, our platform connects you with professionals who value discretion and genuine connection above all else.</p>
                <p>By removing the paywalls common in the industry, we ensure that your search for a partner is based on compatibility, not a subscription model. Join the Harbour City’s premier free network today and experience dating as it was meant to be: effortless, elegant, and entirely focused on the individual.</p>
            '''
        },
        'melbourne': {
            'name': 'Melbourne', 'tag': 'Cultural Sophistication', 'hero_folder': 'melbourne',
            'h2': 'Artistic Soul in the <span>Garden City.</span>',
            'text': '''
                <p>Melbourne is the cultural heartbeat of Australia, a city where laneway discovery meets world-class gastronomy. Dating here is an art form, requiring a platform that appreciates the nuance of a shared interest in the arts, coffee culture, and professional ambition. It is a city of hidden gems, and your partner should be one of them.</p>
                <p>Our Melbourne community is designed for those who find beauty in the details. From the historic elegance of the East End to the vibrant energy of Fitzroy, we provide a space where genuine singles can meet without the distraction of "freemium" gimmicks. GR8Date Melbourne is about finding that person who shares your passion for the city’s unique rhythm, whether that’s a night at the NGV or a weekend exploring the Yarra Valley.</p>
                <p>We prioritize authenticity and safety, ensuring that every match you make in the Garden City is backed by a community that values respect and long-term intentionality. Experience a dating platform that is as sophisticated as your lifestyle.</p>
            '''
        },
        'brisbane': {
            'name': 'Brisbane', 'tag': 'Riverfront Luxury', 'hero_folder': 'brisbane',
            'h2': 'Modern Lifestyle in the <span>Sunshine State.</span>',
            'text': '''
                <p>Brisbane is a city on the rise, blending a relaxed riverfront lifestyle with a rapidly growing professional landscape. Dating in the Sunshine State should feel as bright and effortless as a Sunday morning at Howard Smith Wharves. It is a city that celebrates the outdoors and the modern professional balance.</p>
                <p>GR8Date Brisbane captures this energy by offering a streamlined, professional, and entirely free experience for local singles. We know that Brisbane professionals are looking for more than just a swipe; they are looking for a partner who matches their active, outdoor-oriented, yet career-focused lifestyle. Our platform is the bridge between the casual charm of the River City and the serious pursuit of a life partner.</p>
            '''
        },
        'perth': {
            'name': 'Perth', 'tag': 'Sunset Serenity', 'hero_folder': 'perth',
            'h2': 'Isolated Beauty on the <span>West Coast.</span>',
            'text': '''
                <p>Perth offers a unique dating landscape, defined by its stunning isolation and its wealthy, industrious population. On the West Coast, connections are built on trust and a shared appreciation for the finer things in life—from the white sands of Cottesloe to the premium vineyards of the Swan Valley.</p>
                <p>At GR8Date Perth, we cater to high-profile individuals who require absolute discretion. We understand the "small town" feel of Perth’s professional circles, and our platform is built to provide a private, secure environment where you can explore connections without public exposure. It is about finding a serene partnership that matches the pace of the Indian Ocean sunsets.</p>
            '''
        },
        'adelaide': {
            'name': 'Adelaide', 'tag': 'The Festival City', 'hero_folder': 'adelaide',
            'h2': 'Refined Charm in the <span>Festival City.</span>',
            'text': '<p>Adelaide is a city of churches and world-class wine, requiring a dating platform that understands the value of tradition mixed with modern professional ambition. From the North Terrace cultural precinct to the boutique bars of Peel Street, our network connects Adelaide\'s most intentional singles.</p>'
        },
        'canberra': {
            'name': 'Canberra', 'tag': 'The Capital Standard', 'hero_folder': 'canberra',
            'h2': 'Sophistication in the <span>Nation’s Capital.</span>',
            'text': '<p>In Canberra, discretion is more than a preference—it is a requirement. Our network connects the capital\'s most influential professionals in a secure, private environment. Whether you are strolling through the National Gallery or enjoying the lakeside serenity, find a partner who matches your intellectual and professional drive.</p>'
        },
        'hobart': {
            'name': 'Hobart', 'tag': 'Island Serenity', 'hero_folder': 'hobart',
            'h2': 'Rugged Beauty in <span>Historic Hobart.</span>',
            'text': '<p>From the historic docks of Salamanca to the peaks of Mount Wellington, Hobart dating is defined by authenticity and a slower, more intentional pace. Our platform brings together genuine Tasmanian singles who value quality connections over the quantity of swipes.</p>'
        },
        'darwin': {
            'name': 'Darwin', 'tag': 'Tropical Luxury', 'hero_folder': 'darwin',
            'h2': 'Vibrant Energy in the <span>Top End.</span>',
            'text': '<p>Darwin offers a unique, vibrant lifestyle where tropical luxury meets an adventurous spirit. Our community is built for professionals who enjoy the relaxed pace of the north but demand a high standard of vetting and genuine interaction in their search for a partner.</p>'
        },
        'about': {
            'name': 'About Us', 'tag': 'The GR8Date Story', 'hero_folder': 'sydney',
            'h2': 'Born Out of <span>Frustration.</span>',
            'text': '<p>Welcome to GR8Date, Australia\'s truly <strong>FREE</strong> dating website. Born out of a frustration with paywalls and subscription models, we prioritize people over profit. Our mission is to provide a transparent, authentic space for genuine connection.</p>'
        },
        'privacy': {
            'name': 'Privacy Policy', 'tag': 'Data Security', 'hero_folder': 'melbourne',
            'h2': 'Your Privacy is <span>Important.</span>',
            'text': '<p><strong>1. Compliance:</strong> We operate in accordance with the Privacy Act 1988 (Cth). <strong>2. Data Protection:</strong> We implement industry-standard security to protect your information. <strong>3. Transparency:</strong> We never sell your personal data to third parties.</p>'
        },
        'terms': {
            'name': 'Terms of Service', 'tag': 'User Agreement', 'hero_folder': 'perth',
            'h2': 'Maintaining a <span>Standard.</span>',
            'text': '<p><strong>1. Eligibility:</strong> Users must be 18+. <strong>2. Conduct:</strong> Respect and authenticity are mandatory. <strong>3. Governing Law:</strong> These terms are governed by the laws of New South Wales, Australia.</p>'
        },
        'faq': {
            'name': 'FAQ', 'tag': 'Support', 'hero_folder': 'adelaide',
            'h2': 'Common Questions <span>Answered.</span>',
            'text': '<h3>Why is it free?</h3><p>We believe connection is a right, not a subscription.</p><h3>Is it safe?</h3><p>We use rigorous vetting to maintain a community of genuine professionals.</p>'
        },
        'contact': {
            'name': 'Contact Us', 'tag': 'Support', 'hero_folder': 'brisbane',
            'h2': 'We Are Here to <span>Help.</span>',
            'text': '', 'is_contact': True
        }
    }

    # Fetch data or default to Sydney
    context = city_data.get(city_slug.lower(), city_data['sydney'])
    
    # Send the button-hiding logic to the template
    context['show_join_button'] = not is_legal_page
    
    if city_slug.lower() == 'contact' and request.method == 'POST':
        messages.success(request, f"Thank you, {request.POST.get('name')}. Message sent.")

    return render(request, 'city_landing.html', context)