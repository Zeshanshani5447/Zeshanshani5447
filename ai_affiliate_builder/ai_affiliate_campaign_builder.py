#!/usr/bin/env python3
"""
AI Affiliate Campaign Builder
Generate complete affiliate marketing campaigns using AI simulation.
No experience needed - beginner friendly!
"""

import json
import random
from datetime import datetime

class AIAffiliateCampaignBuilder:
    def __init__(self):
        self.niches = [
            "Health & Fitness",
            "Make Money Online",
            "Technology & Gadgets",
            "Beauty & Skincare",
            "Home & Garden",
            "Pet Care",
            "Travel",
            "Personal Finance"
        ]
        
        self.product_types = {
            "Health & Fitness": ["Weight Loss Supplements", "Fitness Equipment", "Workout Programs", "Nutrition Plans"],
            "Make Money Online": ["Online Courses", "Software Tools", "E-books", "Membership Sites"],
            "Technology & Gadgets": ["Smart Home Devices", "Gaming Accessories", "Productivity Software", "Tech Gadgets"],
            "Beauty & Skincare": ["Anti-Aging Creams", "Organic Skincare", "Makeup Products", "Hair Care Solutions"],
            "Home & Garden": ["Garden Tools", "Home Decor", "Kitchen Gadgets", "Cleaning Products"],
            "Pet Care": ["Pet Supplements", "Training Programs", "Pet Accessories", "Organic Pet Food"],
            "Travel": ["Travel Gear", "Booking Platforms", "Travel Insurance", "Luggage"],
            "Personal Finance": ["Investment Platforms", "Budgeting Apps", "Credit Cards", "Financial Courses"]
        }
        
        self.content_templates = {
            "blog_post": [
                "Top 10 {product} for {year} - Complete Review & Buying Guide",
                "How I Lost 20 Pounds Using {product} - My Honest Review",
                "{product} Review: Is It Worth The Hype? (Full Analysis)",
                "The Ultimate Guide to Choosing the Best {product} in {year}",
                "5 Reasons Why {product} Changed My Life Forever"
            ],
            "social_media": [
                "🔥 Just discovered this amazing {product}! Game changer! #affiliate #review",
                "Can't believe the results I got with {product}! Link in bio 👆",
                "Stop wasting money on fake products. This {product} actually works! 💯",
                "My secret weapon for success: {product}. Try it now!",
                "Limited time offer on {product}! Don't miss out! 🚀"
            ],
            "email_subject": [
                "You need to see this {product} review...",
                "My honest thoughts about {product}",
                "Special discount inside: {product}",
                "How {product} changed everything for me",
                "Last chance: {product} at 50% off!"
            ]
        }
        
        self.cta_phrases = [
            "Get Yours Now",
            "Claim Your Discount",
            "Start Today",
            "Try Risk-Free",
            "Limited Offer - Act Fast",
            "Join Thousands of Happy Customers",
            "Transform Your Life Today"
        ]
        
        self.audience_pain_points = {
            "Health & Fitness": ["struggling to lose weight", "no time for gym", "confused by diet trends", "low energy levels"],
            "Make Money Online": ["stuck in 9-5 job", "need extra income", "want financial freedom", "tired of scams"],
            "Technology & Gadgets": ["overwhelmed by choices", "need better productivity", "want latest tech", "budget constraints"],
            "Beauty & Skincare": ["aging concerns", "sensitive skin issues", "expensive products", "confusing routines"],
            "Home & Garden": ["small space challenges", "lack of time", "budget renovations", "maintenance struggles"],
            "Pet Care": ["pet behavior issues", "health concerns", "expensive vet bills", "finding quality products"],
            "Travel": ["budget travel needs", "safety concerns", "packing struggles", "planning overwhelm"],
            "Personal Finance": ["debt problems", "saving difficulties", "investment confusion", "retirement worries"]
        }
    
    def generate_campaign_name(self, niche):
        """Generate a catchy campaign name"""
        adjectives = ["Ultimate", "Pro", "Smart", "Quick", "Easy", "Premium", "Elite", "Express"]
        nouns = ["Solution", "System", "Blueprint", "Formula", "Method", "Strategy", "Guide", "Plan"]
        return f"{random.choice(adjectives)} {niche.split()[0]} {random.choice(nouns)}"
    
    def generate_target_audience(self, niche):
        """Define target audience for the niche"""
        pain_points = self.audience_pain_points.get(niche, ["general concerns"])
        return {
            "demographics": "Adults 25-55 interested in " + niche.lower(),
            "pain_points": random.sample(pain_points, min(3, len(pain_points))),
            "goals": [f"Find reliable {niche.lower()} solutions", "Save time and money", "Get proven results"]
        }
    
    def generate_content_piece(self, content_type, niche, product):
        """Generate content based on type"""
        templates = self.content_templates.get(content_type, [])
        if not templates:
            return "Content template not available"
        
        template = random.choice(templates)
        content = template.replace("{product}", product).replace("{year}", str(datetime.now().year))
        
        # Add CTA
        cta = random.choice(self.cta_phrases)
        content += f"\n\n👉 {cta}!"
        
        return content
    
    def generate_email_sequence(self, niche, product):
        """Generate a 5-email sequence"""
        emails = []
        subjects = random.sample(self.content_templates["email_subject"], 5)
        
        email_bodies = [
            f"Hey there!\n\nI wanted to share something that completely changed my approach to {niche.lower()}.\n\nAfter trying countless solutions, I finally found {product} - and the results have been incredible!\n\n{random.choice(self.cta_phrases)}: [Your Affiliate Link]\n\nBest regards,\n[Your Name]",
            
            f"Hi again!\n\nRemember how I mentioned {product} yesterday?\n\nWell, I got so many questions that I decided to write a full review.\n\nHere's what makes it different from everything else...\n\n[Your Affiliate Link]\n\nTalk soon!",
            
            f"Hello!\n\nQuick question: Are you still struggling with {random.choice(self.audience_pain_points.get(niche, ['this']))}?\n\nI was too, until I discovered {product}.\n\nDon't take my word for it - see the results yourself:\n\n[Your Affiliate Link]",
            
            f"Hey!\n\nI almost forgot to mention - there's a special discount available right now for {product}!\n\nThis won't last long, so if you've been thinking about it...\n\nNow's the time: [Your Affiliate Link]",
            
            f"Last chance!\n\nThis is my final email about {product}.\n\nIf you're ready to finally solve your {niche.lower()} challenges, this is your opportunity.\n\nGet it here before the offer expires: [Your Affiliate Link]\n\nWishing you success!"
        ]
        
        for i in range(5):
            emails.append({
                "day": i + 1,
                "subject": subjects[i],
                "body": email_bodies[i]
            })
        
        return emails
    
    def generate_social_media_plan(self, niche, product):
        """Generate 7-day social media plan"""
        platforms = ["Instagram", "Facebook", "Twitter", "LinkedIn", "TikTok"]
        posts = []
        
        for day in range(7):
            post = {
                "day": day + 1,
                "platform": random.choice(platforms),
                "content": self.generate_content_piece("social_media", niche, product),
                "hashtags": f"#{niche.replace(' ', '')} #AffiliateMarketing #ProductReview #Sponsored",
                "best_time": random.choice(["9:00 AM", "12:00 PM", "6:00 PM", "8:00 PM"])
            }
            posts.append(post)
        
        return posts
    
    def build_complete_campaign(self, niche=None):
        """Build a complete affiliate campaign"""
        if not niche:
            niche = random.choice(self.niches)
        
        products = self.product_types.get(niche, ["Generic Product"])
        product = random.choice(products)
        
        campaign = {
            "campaign_name": self.generate_campaign_name(niche),
            "niche": niche,
            "featured_product": product,
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "target_audience": self.generate_target_audience(niche),
            "content_pieces": {
                "blog_posts": [self.generate_content_piece("blog_post", niche, product) for _ in range(3)],
                "social_media_posts": self.generate_social_media_plan(niche, product),
                "email_sequence": self.generate_email_sequence(niche, product)
            },
            "recommended_ctas": random.sample(self.cta_phrases, 3),
            "success_tips": [
                "Always disclose your affiliate relationships",
                "Provide genuine value before promoting",
                "Test different content formats",
                "Track your clicks and conversions",
                "Build trust with your audience first"
            ]
        }
        
        return campaign
    
    def save_campaign(self, campaign, filename="affiliate_campaign.json"):
        """Save campaign to JSON file"""
        with open(filename, 'w') as f:
            json.dump(campaign, f, indent=2)
        print(f"✅ Campaign saved to {filename}")
    
    def display_campaign(self, campaign):
        """Display campaign in a readable format"""
        print("\n" + "="*60)
        print("🚀 YOUR AI-GENERATED AFFILIATE CAMPAIGN")
        print("="*60)
        print(f"\n📋 Campaign Name: {campaign['campaign_name']}")
        print(f"🎯 Niche: {campaign['niche']}")
        print(f"💼 Featured Product: {campaign['featured_product']}")
        print(f"📅 Created: {campaign['created_at']}")
        
        print("\n👥 TARGET AUDIENCE:")
        audience = campaign['target_audience']
        print(f"   Demographics: {audience['demographics']}")
        print(f"   Pain Points: {', '.join(audience['pain_points'])}")
        print(f"   Goals: {', '.join(audience['goals'])}")
        
        print("\n📝 BLOG POST IDEAS:")
        for i, post in enumerate(campaign['content_pieces']['blog_posts'], 1):
            print(f"\n   [{i}] {post.split(chr(10))[0]}")
        
        print("\n📱 SOCIAL MEDIA PLAN (7 Days):")
        for post in campaign['content_pieces']['social_media_posts']:
            print(f"\n   Day {post['day']} - {post['platform']} @ {post['best_time']}")
            print(f"   Content: {post['content'][:100]}...")
        
        print("\n📧 EMAIL SEQUENCE (5 Emails):")
        for email in campaign['content_pieces']['email_sequence']:
            print(f"\n   Day {email['day']}: {email['subject']}")
        
        print("\n🎯 RECOMMENDED CTAs:")
        for cta in campaign['recommended_ctas']:
            print(f"   • {cta}")
        
        print("\n💡 SUCCESS TIPS:")
        for tip in campaign['success_tips']:
            print(f"   ✓ {tip}")
        
        print("\n" + "="*60)
        print("✨ Ready to start earning! Just add your affiliate links!")
        print("="*60 + "\n")


def main():
    print("\n" + "🎉"*20)
    print("Welcome to AI Affiliate Campaign Builder!")
    print("Create complete affiliate campaigns in minutes - No experience needed!")
    print("🎉"*20 + "\n")
    
    builder = AIAffiliateCampaignBuilder()
    
    print("Available Niches:")
    for i, niche in enumerate(builder.niches, 1):
        print(f"  {i}. {niche}")
    print(f"  {len(builder.niches) + 1}. Random Surprise Niche")
    
    choice = input(f"\nSelect a niche (1-{len(builder.niches) + 1}): ").strip()
    
    if choice.isdigit():
        choice_num = int(choice)
        if 1 <= choice_num <= len(builder.niches):
            niche = builder.niches[choice_num - 1]
        elif choice_num == len(builder.niches) + 1:
            niche = None
            print("🎲 Generating random niche campaign...")
        else:
            print("Invalid choice. Using random niche.")
            niche = None
    else:
        print("Using random niche.")
        niche = None
    
    print("\n⚡ Building your campaign...")
    campaign = builder.build_complete_campaign(niche)
    
    builder.display_campaign(campaign)
    
    save_choice = input("\nWould you like to save this campaign? (y/n): ").strip().lower()
    if save_choice == 'y':
        filename = input("Enter filename (default: affiliate_campaign.json): ").strip()
        if not filename:
            filename = "affiliate_campaign.json"
        builder.save_campaign(campaign, filename)
    
    print("\n🙏 Thank you for using AI Affiliate Campaign Builder!")
    print("Remember: Success comes from taking action. Start implementing today!")
    print("\n" + "🚀"*20 + "\n")


if __name__ == "__main__":
    main()
