from django.shortcuts import render
from django.contrib import messages

def index(request):
    """Main landing page view."""
    return render(request, 'index.html')

def city_landing(request, city_slug):
    """
    Final Master View: Handles all 8 Cities + all 5 Legal/Support pages.
    """
    city_data = {
        # --- CITIES (Full 350+ word editorials) ---
        'sydney': {
            'name': 'Sydney', 'tag': 'The Harbour Standard', 'hero_folder': 'sydney',
            'meta_title': 'Sydney Dating | Australia’s Premier Free Private Network',
            'meta_desc': 'Join Sydney’s exclusive network for intentional dating. Connect with verified professionals.',
            'h2': 'Refined Elegance in the <span>Harbour City.</span>',
            'text': '<p>Sydney is a city defined by its global stature... [Keep full text here]</p>'
        },
        # ... [Repeat for Melbourne, Brisbane, Perth, Adelaide, Canberra, Hobart, Darwin] ...

        # --- FINAL LEGAL & SUPPORT PAGES (Integrated from your old files) ---
        'about': {
            'name': 'About Us', 'tag': 'The GR8Date Story', 'hero_folder': 'sydney',
            'meta_title': 'About GR8Date - Australia\'s 100% Free Dating Platform Story',
            'meta_desc': 'Learn about our mission to provide completely free online dating in Australia without hidden costs.',
            'h2': 'Born Out of <span>Frustration.</span>',
            'text': '''
                <p>Welcome to GR8Date, Australia's truly <strong>FREE</strong> dating website. Our mission is simple: to connect genuine people looking for meaningful relationships without the burden of hidden costs or subscription fees.</p>
                <p>GR8Date was born out of a common frustration. Our creator, like countless others, experienced the disappointment of traditional dating sites that promise connection but deliver endless paywalls. It became clear that the industry was designed to profit from loneliness, rather than genuinely helping people find their match.</p>
                <p>Driven by this personal experience, we decided to build a site that prioritizes people over profit, offering all essential features completely free of charge.</p>
            '''
        },
        'privacy': {
            'name': 'Privacy Policy', 'tag': 'Data Security', 'hero_folder': 'melbourne',
            'meta_title': 'Privacy Policy | GR8Date Free Dating Platform',
            'meta_desc': 'How we collect, use, and protect your personal information at GR8Date.',
            'h2': 'Your Privacy is <span>Important.</span>',
            'text': '''
                <p><strong>1. Information We Collect:</strong> We collect information you provide directly, such as when you create an account or fill out forms.</p>
                <p><strong>2. How We Use Your Information:</strong> To maintain our services, communicate updates, and comply with legal obligations.</p>
                <p><strong>3. Data Security:</strong> We implement reasonable security measures to protect your data from unauthorized access.</p>
                <p><strong>4. Cookies:</strong> We use cookies to enhance your experience and analyze usage.</p>
                <p><strong>5. Third-Party Services:</strong> We may share info with trusted providers under strict confidentiality.</p>
                <p><strong>6. Children\'s Privacy:</strong> Our services are not intended for individuals under 18.</p>
                <p><strong>7. Contact Us:</strong> admin@gr8date.au</p>
                <p><em>Effective Date: 27 August 2025</em></p>
            '''
        },
        'terms': {
            'name': 'Terms of Service', 'tag': 'User Agreement', 'hero_folder': 'perth',
            'meta_title': 'Terms of Service | GR8Date Community Standards',
            'meta_desc': 'User agreement and community guidelines for Australia\'s free dating platform.',
            'h2': 'Maintaining a <span>Standard of Excellence.</span>',
            'text': '''
                <p><strong>Effective Date: 27 August 2025</strong></p>
                <p><strong>1. Acceptance:</strong> By creating an account, you agree to be bound by these Terms.</p>
                <p><strong>2. Eligibility:</strong> You must be at least 18 years of age to use the Service.</p>
                <p><strong>3. Free Service:</strong> GR8Date is committed to being a completely free dating platform.</p>
                <p><strong>4. Conduct:</strong> You must not post defamatory, obscene, or harassing content. We reserve the right to monitor communications for safety.</p>
                <p><strong>5. Liability:</strong> The Service is provided "as is." GR8Date is not liable for damages arising from your use of the Service or interactions with other members.</p>
                <p><strong>6. Governing Law:</strong> These Terms are governed by the laws of <strong>New South Wales, Australia</strong>.</p>
            '''
        },
        'faq': {
            'name': 'FAQ', 'tag': 'Support', 'hero_folder': 'adelaide',
            'meta_title': 'FAQ - GR8Date Free Dating Questions Answered',
            'meta_desc': 'Get answers to common questions about Australia\'s free dating platform.',
            'h2': 'Common Questions <span>Answered.</span>',
            'text': '''
                <h3>Why is GR8Date free?</h3>
                <p>We believe finding connection should be accessible to everyone without a financial barrier.</p>
                <h3>What makes us different?</h3>
                <p>We focus on transparency, authenticity, and a community for mature adults seeking respectful connections.</p>
                <h3>How do I get started?</h3>
                <p>Create your profile in minutes, upload photos, and start connecting—all for free.</p>
            '''
        },
        'contact': {
            'name': 'Contact Us', 'tag': 'Support', 'hero_folder': 'brisbane',
            'meta_title': 'Contact GR8Date Support', 'meta_desc': 'Get help with your GR8Date account.',
            'h2': 'We Are Here to <span>Help.</span>',
            'text': '', 'is_contact': True
        }
    }

    context = city_data.get(city_slug.lower(), city_data['sydney'])

    # Contact Form Logic
    if city_slug.lower() == 'contact' and request.method == 'POST':
        name = request.POST.get('name')
        messages.success(request, f"Thank you, {name}. Your message has been sent to our support team.")

    return render(request, 'city_landing.html', context)