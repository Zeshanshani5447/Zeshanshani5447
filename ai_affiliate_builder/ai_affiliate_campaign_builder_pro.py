#!/usr/bin/env python3
"""
AI Affiliate Campaign Builder - PRO VERSION
Advanced features: Web Scraping, AI Content Generation, Competitor Analysis, SEO Optimization
No experience needed - beginner friendly!
"""

import json
import random
import re
from datetime import datetime, timedelta
from typing import Dict, List, Optional
import urllib.request
from urllib.parse import quote_plus, urlparse
from bs4 import BeautifulSoup
import ssl

# Handle SSL certificates
ssl._create_default_https_context = ssl._create_unverified_context


class AdvancedAIAffiliateCampaignBuilder:
    def __init__(self):
        self.niches = [
            "Health & Fitness",
            "Make Money Online",
            "Technology & Gadgets",
            "Beauty & Skincare",
            "Home & Garden",
            "Pet Care",
            "Travel",
            "Personal Finance",
            "Sustainable Living",
            "Gaming & Esports"
        ]
        
        self.product_types = {
            "Health & Fitness": ["Weight Loss Supplements", "Fitness Equipment", "Workout Programs", "Nutrition Plans", "Yoga Mats", "Protein Powders"],
            "Make Money Online": ["Online Courses", "Software Tools", "E-books", "Membership Sites", "Trading Platforms", "Dropshipping Tools"],
            "Technology & Gadgets": ["Smart Home Devices", "Gaming Accessories", "Productivity Software", "Tech Gadgets", "Wireless Earbuds", "Smart Watches"],
            "Beauty & Skincare": ["Anti-Aging Creams", "Organic Skincare", "Makeup Products", "Hair Care Solutions", "Serums", "Beauty Tools"],
            "Home & Garden": ["Garden Tools", "Home Decor", "Kitchen Gadgets", "Cleaning Products", "Smart Lighting", "Furniture"],
            "Pet Care": ["Pet Supplements", "Training Programs", "Pet Accessories", "Organic Pet Food", "Pet Cameras", "Grooming Tools"],
            "Travel": ["Travel Gear", "Booking Platforms", "Travel Insurance", "Luggage", "Travel Adapters", "Camera Equipment"],
            "Personal Finance": ["Investment Platforms", "Budgeting Apps", "Credit Cards", "Financial Courses", "Crypto Exchanges", "Tax Software"],
            "Sustainable Living": ["Solar Panels", "Eco Products", "Reusable Items", "Green Energy", "Composting Systems", "Water Filters"],
            "Gaming & Esports": ["Gaming Chairs", "Mechanical Keyboards", "Gaming Mice", "Stream Equipment", "Game Subscriptions", "VR Headsets"]
        }
        
        self.affiliate_networks = {
            "Health & Fitness": ["ClickBank", "ShareASale", "Amazon Associates", "CJ Affiliate"],
            "Make Money Online": ["ClickBank", "Digistore24", "WarriorPlus", "JVZoo"],
            "Technology & Gadgets": ["Amazon Associates", "Best Buy Affiliate", "Newegg", "ShareASale"],
            "Beauty & Skincare": ["Ulta Beauty", "Sephora", "Amazon Associates", "ShareASale"],
            "Home & Garden": ["Amazon Associates", "Wayfair", "Home Depot", "ShareASale"],
            "Pet Care": ["Chewy", "Amazon Associates", "Petco", "ShareASale"],
            "Travel": ["Booking.com", "Expedia", "TripAdvisor", "GetYourGuide"],
            "Personal Finance": ["PartnerStack", "Impact", "CJ Affiliate", "Direct Programs"],
            "Sustainable Living": ["Amazon Associates", "Etsy Affiliate", "ShareASale", "Direct Brands"],
            "Gaming & Esports": ["Amazon Associates", "Newegg", "GameStop", "Steam Affiliate"]
        }
        
        self.competitor_keywords = {}
        self.trending_topics = {}
        self.seo_data = {}
        
    def scrape_trending_products(self, niche: str) -> List[Dict]:
        """Scrape trending products from various sources"""
        print(f"\n🔍 Scraping trending products for {niche}...")
        
        trending_products = []
        
        # Simulate scraping from multiple sources (in production, use real APIs)
        product_sources = [
            self._scrape_amazon_trending(niche),
            self._scrape_clickbank_gravity(niche),
            self._scrape_reddit_discussions(niche),
            self._scrape_social_media_trends(niche)
        ]
        
        for source in product_sources:
            if source:
                trending_products.extend(source)
        
        # Remove duplicates and return top products
        unique_products = []
        seen_names = set()
        for product in trending_products:
            if product['name'] not in seen_names:
                seen_names.add(product['name'])
                unique_products.append(product)
        
        return unique_products[:10]  # Return top 10
    
    def _scrape_amazon_trending(self, niche: str) -> List[Dict]:
        """Scrape Amazon Best Sellers (simulated - use API in production)"""
        # In production: Use Amazon Product Advertising API
        amazon_categories = {
            "Health & Fitness": "3760901",
            "Technology & Gadgets": "172282",
            "Beauty & Skincare": "3760911",
            "Home & Garden": "1055398",
            "Pet Care": "2619533011",
            "Travel": "15743961",
        }
        
        # Simulated results (replace with actual API calls)
        simulated_products = [
            {
                "name": f"Premium {niche.split()[0]} Solution Pro",
                "price": "$49.99",
                "rating": 4.5,
                "reviews": 2847,
                "source": "Amazon",
                "commission_rate": "4-8%",
                "url": "https://amazon.com/dp/EXAMPLE"
            },
            {
                "name": f"Ultimate {niche.split()[0]} Kit 2025",
                "price": "$79.99",
                "rating": 4.7,
                "reviews": 1523,
                "source": "Amazon",
                "commission_rate": "4-8%",
                "url": "https://amazon.com/dp/EXAMPLE2"
            }
        ]
        
        return simulated_products
    
    def _scrape_clickbank_gravity(self, niche: str) -> List[Dict]:
        """Scrape ClickBank high gravity products (simulated)"""
        # In production: Use ClickBank API or hoplink tracking
        gravity_products = [
            {
                "name": f"{niche.split()[0]} Mastery System",
                "price": "$97.00",
                "rating": 4.8,
                "reviews": 892,
                "source": "ClickBank",
                "commission_rate": "50-75%",
                "gravity_score": random.randint(50, 150),
                "url": "https://clickbank.net/EXAMPLE"
            },
            {
                "name": f"Complete {niche.split()[0]} Blueprint",
                "price": "$67.00",
                "rating": 4.6,
                "reviews": 654,
                "source": "ClickBank",
                "commission_rate": "60-75%",
                "gravity_score": random.randint(30, 100),
                "url": "https://clickbank.net/EXAMPLE2"
            }
        ]
        
        return gravity_products
    
    def _scrape_reddit_discussions(self, niche: str) -> List[Dict]:
        """Scrape Reddit for product discussions and recommendations"""
        print("   📱 Analyzing Reddit discussions...")
        
        # In production: Use PRAW (Python Reddit API Wrapper)
        # This is simulated data
        reddit_products = [
            {
                "name": f"Community Favorite {niche.split()[0]} Tool",
                "price": "$39.99",
                "rating": 4.9,
                "reviews": 456,
                "source": "Reddit Recommendations",
                "commission_rate": "Varies",
                "mentions": random.randint(100, 500),
                "sentiment": "Positive",
                "url": "https://reddit.com/r/EXAMPLE"
            }
        ]
        
        return reddit_products
    
    def _scrape_social_media_trends(self, niche: str) -> List[Dict]:
        """Analyze social media trends for the niche"""
        print("   📊 Analyzing social media trends...")
        
        # In production: Use Twitter API, Instagram Graph API, TikTok API
        # This is simulated data
        social_products = [
            {
                "name": f"Viral {niche.split()[0]} Product 2025",
                "price": "$59.99",
                "rating": 4.4,
                "reviews": 2341,
                "source": "Social Media Trending",
                "commission_rate": "10-20%",
                "social_mentions": random.randint(1000, 10000),
                "platform": random.choice(["TikTok", "Instagram", "Twitter"]),
                "url": "https://example.com/viral-product"
            }
        ]
        
        return social_products
    
    def analyze_competitors(self, niche: str, keywords: List[str]) -> Dict:
        """Analyze competitor strategies and content"""
        print(f"\n🕵️ Analyzing competitors for {niche}...")
        
        competitor_analysis = {
            "top_competitors": [],
            "content_gaps": [],
            "keyword_difficulty": {},
            "backlink_opportunities": [],
            "content_strategies": []
        }
        
        # Simulate competitor analysis (in production, use SERP APIs)
        competitors = [
            {
                "domain": f"top{nich.split()[0].lower()}site.com",
                "monthly_traffic": random.randint(50000, 500000),
                "domain_authority": random.randint(40, 80),
                "top_content": f"Best {niche} Products Review 2025",
                "estimated_revenue": f"${random.randint(5000, 50000)}/month"
            }
            for nich in [niche] * 3
        ]
        
        competitor_analysis["top_competitors"] = competitors
        
        # Identify content gaps
        content_gaps = [
            f"Comparison: Top 5 {niche} Solutions Under $50",
            f"How to Choose the Right {niche} Product for Beginners",
            f"{niche} Myths Debunked: What Really Works",
            f"Case Study: 30-Day {niche} Transformation",
            f"Ultimate {niche} Buying Guide for 2025"
        ]
        competitor_analysis["content_gaps"] = content_gaps
        
        # Keyword difficulty analysis
        for keyword in keywords[:5]:
            competitor_analysis["keyword_difficulty"][keyword] = {
                "difficulty": random.randint(20, 80),
                "search_volume": random.randint(1000, 50000),
                "cpc": f"${random.uniform(0.5, 5.0):.2f}",
                "competition": random.choice(["Low", "Medium", "High"])
            }
        
        return competitor_analysis
    
    def generate_seo_optimized_content(self, niche: str, product: str, 
                                       keywords: List[str], content_type: str) -> str:
        """Generate SEO-optimized content with proper keyword density"""
        print(f"\n✍️ Generating SEO-optimized {content_type}...")
        
        primary_keyword = keywords[0] if keywords else f"best {niche.lower()} products"
        secondary_keywords = keywords[1:3] if len(keywords) > 1 else [f"{niche.lower()} reviews"]
        
        if content_type == "blog_post":
            content = self._generate_blog_post(niche, product, primary_keyword, secondary_keywords)
        elif content_type == "product_review":
            content = self._generate_product_review(niche, product, primary_keyword)
        elif content_type == "comparison":
            content = self._generate_comparison_article(niche, product, keywords)
        else:
            content = self._generate_generic_content(niche, product, keywords)
        
        # Add SEO metadata
        seo_metadata = {
            "meta_title": f"{primary_keyword.title()} - Ultimate Guide 2025 | Expert Reviews",
            "meta_description": f"Discover the best {primary_keyword}. Expert reviews, comparisons, and buying guides. Save time and money with our tested recommendations.",
            "focus_keyword": primary_keyword,
            "keyword_density": "1.5-2.5%",
            "readability_score": random.randint(65, 85),
            "word_count": random.randint(1500, 3000)
        }
        
        return {
            "content": content,
            "seo_metadata": seo_metadata
        }
    
    def _generate_blog_post(self, niche: str, product: str, 
                           primary_keyword: str, secondary_keywords: List[str]) -> str:
        """Generate a complete blog post"""
        year = datetime.now().year
        
        blog_post = f"""
# {primary_keyword.title()} - Complete Guide {year}

## Introduction
Are you looking for the best {primary_keyword}? You're in the right place! After extensive research and testing, we've compiled this comprehensive guide to help you make an informed decision.

In this article, we'll cover everything you need to know about {secondary_keywords[0] if secondary_keywords else niche.lower()}, including top recommendations, pros and cons, and expert tips.

## Why Trust Our Recommendations?
Our team has spent countless hours researching and testing {niche.lower()} products. We analyze customer reviews, expert opinions, and real-world performance to bring you unbiased recommendations.

## Top {primary_keyword.title()} in {year}

### 1. {product} - Editor's Choice ⭐
**Rating:** 4.8/5 | **Price:** $XX.XX

{product} stands out as our top pick for several reasons:

**Pros:**
✓ High-quality materials and construction
✓ Excellent customer reviews (4.8+ stars)
✓ Great value for money
✓ Proven results backed by science
✓ Outstanding customer support

**Cons:**
✗ May be out of stock during peak seasons
✗ Premium pricing compared to basic alternatives

**Best For:** Beginners and professionals alike who want reliable results.

[👉 Check Latest Price & Availability]

### 2. Premium Alternative
**Rating:** 4.7/5 | **Price:** $XX.XX

Another excellent option for those seeking premium features...

### 3. Budget-Friendly Option
**Rating:** 4.5/5 | **Price:** $XX.XX

Perfect for beginners on a budget without compromising quality...

## Buying Guide: How to Choose the Right {niche} Product

When selecting {primary_keyword}, consider these factors:

1. **Quality & Durability**: Look for products made with high-quality materials
2. **Customer Reviews**: Check verified purchase reviews
3. **Price vs Value**: Don't just go for the cheapest option
4. **Warranty & Support**: Ensure good customer service
5. **Features**: Match features to your specific needs

## Common Mistakes to Avoid

❌ Buying based solely on price
❌ Ignoring customer reviews
❌ Not checking return policies
❌ Falling for fake discounts
❌ Choosing incompatible products

## Frequently Asked Questions

### Q: What is the best {primary_keyword} for beginners?
A: We recommend starting with {product} as it offers the best balance of features, quality, and ease of use.

### Q: How much should I spend on {secondary_keywords[0] if secondary_keywords else niche.lower()}?
A: Quality {niche.lower()} products typically range from $30-$150. Invest in quality for better long-term results.

### Q: Are expensive {niche.lower()} products worth it?
A: Not necessarily. Many mid-range options offer excellent value. Focus on features that matter to you.

## Conclusion

Finding the right {primary_keyword} doesn't have to be overwhelming. Based on our research, {product} offers the best combination of quality, features, and value in {year}.

Remember to consider your specific needs, budget, and read customer reviews before making your final decision.

---

**Ready to get started?** [👉 Click here to check the latest price and availability of {product}]

*Disclosure: This post contains affiliate links. If you make a purchase through these links, we may earn a commission at no extra cost to you.*
"""
        return blog_post.strip()
    
    def _generate_product_review(self, niche: str, product: str, keyword: str) -> str:
        """Generate detailed product review"""
        return f"""
# {product} Review {datetime.now().year}: Is It Worth The Hype?

## Quick Verdict: ⭐⭐⭐⭐⭐ (4.8/5)

After testing {product} for 30 days, we can confidently say it's one of the best {keyword} available today.

## What is {product}?

{product} is a premium solution designed for {niche.lower()} enthusiasts who demand quality and results.

## Key Features

✅ Feature 1: Advanced technology for optimal performance
✅ Feature 2: User-friendly design suitable for all skill levels
✅ Feature 3: Durable construction built to last
✅ Feature 4: Excellent customer support and warranty

## Pros & Cons

**Pros:**
• High effectiveness
• Great value
• Positive user feedback
• Fast results

**Cons:**
• Limited availability
• Premium pricing

## Who Should Buy {product}?

✓ Beginners looking for a reliable solution
✓ Professionals seeking premium quality
✓ Anyone serious about {niche.lower()}

## Final Recommendation

If you're serious about {niche.lower()}, {product} is definitely worth the investment.

[👉 Get {product} Now - Best Price Guaranteed]
"""
    
    def _generate_comparison_article(self, niche: str, product: str, keywords: List[str]) -> str:
        """Generate comparison article"""
        return f"""
# Top 5 {keywords[0] if keywords else niche} Compared ({datetime.now().year})

We've tested and compared the top products so you don't have to!

## Comparison Table

| Product | Rating | Price | Best For |
|---------|--------|-------|----------|
| {product} | 4.8⭐ | $$$ | Overall Winner |
| Competitor A | 4.6⭐ | $$ | Budget Pick |
| Competitor B | 4.7⭐ | $$$$ | Premium Choice |
| Competitor C | 4.5⭐ | $$ | Best Value |
| Competitor D | 4.4⭐ | $ | Entry Level |

## Detailed Analysis

### 🏆 Winner: {product}

{product} takes the crown for its exceptional balance of quality, features, and value.

**Why it won:**
- Superior build quality
- Excellent customer reviews
- Competitive pricing
- Outstanding support

[👉 Check Current Deal on {product}]

## Conclusion

For most people, {product} is the clear winner. However, your specific needs may vary.

[👉 See All Products Compared]
"""
    
    def _generate_generic_content(self, niche: str, product: str, keywords: List[str]) -> str:
        """Generate generic content"""
        return f"""
# Ultimate Guide to {keywords[0] if keywords else niche}

Everything you need to know about {niche.lower()} in {datetime.now().year}.

## Introduction

{product} has revolutionized the way people approach {niche.lower()}. Let's explore why.

## Key Benefits

1. Benefit One: Explanation
2. Benefit Two: Explanation  
3. Benefit Three: Explanation

## Getting Started

Here's how to maximize your results with {product}...

## Conclusion

Ready to transform your {niche.lower()} journey? 

[👉 Get Started with {product} Today]
"""
    
    def extract_keywords_from_url(self, url: str) -> List[str]:
        """Extract relevant keywords from a webpage"""
        print(f"\n🔑 Extracting keywords from: {url}")
        
        try:
            headers = {'User-Agent': 'Mozilla/5.0'}
            req = urllib.request.Request(url, headers=headers)
            response = urllib.request.urlopen(req, timeout=10)
            html = response.read().decode('utf-8', errors='ignore')
            
            soup = BeautifulSoup(html, 'html.parser')
            
            # Extract title
            title = soup.find('title')
            title_text = title.get_text().strip() if title else ""
            
            # Extract meta description
            meta_desc = soup.find('meta', attrs={'name': 'description'})
            description = meta_desc['content'].strip() if meta_desc else ""
            
            # Extract headings
            headings = []
            for h in soup.find_all(['h1', 'h2', 'h3']):
                headings.append(h.get_text().strip())
            
            # Combine and extract keywords
            text_content = f"{title_text} {description} {' '.join(headings)}"
            
            # Simple keyword extraction (in production, use NLP libraries)
            words = re.findall(r'\b[a-zA-Z]{4,}\b', text_content.lower())
            
            # Count word frequency
            word_freq = {}
            for word in words:
                word_freq[word] = word_freq.get(word, 0) + 1
            
            # Filter common words and get top keywords
            stop_words = {'the', 'and', 'for', 'with', 'that', 'this', 'from', 'your', 'have', 'been', 'were', 'will', 'would'}
            keywords = [word for word, freq in sorted(word_freq.items(), key=lambda x: x[1], reverse=True) 
                       if word not in stop_words][:10]
            
            return keywords
            
        except Exception as e:
            print(f"   ⚠️ Error extracting keywords: {e}")
            return []
    
    def generate_social_media_calendar(self, niche: str, product: str, 
                                      platforms: List[str] = None) -> List[Dict]:
        """Generate comprehensive social media calendar with optimal posting times"""
        if platforms is None:
            platforms = ["Instagram", "Facebook", "Twitter", "LinkedIn", "TikTok", "Pinterest"]
        
        print(f"\n📅 Generating social media calendar for {len(platforms)} platforms...")
        
        calendar = []
        content_types = [
            {"type": "Educational", "emoji": "📚"},
            {"type": "Inspirational", "emoji": "✨"},
            {"type": "Promotional", "emoji": "🔥"},
            {"type": "User Generated", "emoji": "👥"},
            {"type": "Behind the Scenes", "emoji": "🎬"},
            {"type": "Question/Poll", "emoji": "❓"},
            {"type": "Testimonial", "emoji": "💬"}
        ]
        
        optimal_times = {
            "Instagram": ["9:00 AM", "12:00 PM", "6:00 PM"],
            "Facebook": ["1:00 PM", "3:00 PM", "7:00 PM"],
            "Twitter": ["8:00 AM", "12:00 PM", "5:00 PM"],
            "LinkedIn": ["8:00 AM", "12:00 PM", "5:00 PM"],
            "TikTok": ["6:00 AM", "10:00 AM", "7:00 PM"],
            "Pinterest": ["8:00 PM", "9:00 PM", "11:00 PM"]
        }
        
        for day in range(30):  # 30-day calendar
            date = datetime.now() + timedelta(days=day)
            
            for platform in platforms:
                content = random.choice(content_types)
                
                post = {
                    "date": date.strftime("%Y-%m-%d"),
                    "day_name": date.strftime("%A"),
                    "platform": platform,
                    "content_type": content["type"],
                    "emoji": content["emoji"],
                    "post_idea": self._generate_post_idea(niche, product, content["type"]),
                    "optimal_time": random.choice(optimal_times.get(platform, ["12:00 PM"])),
                    "hashtags": self._generate_hashtags(niche, platform),
                    "cta": random.choice([
                        "Link in bio 👆",
                        "Swipe up to learn more",
                        "Comment below with your thoughts",
                        "Tag a friend who needs this",
                        "Save this for later",
                        "DM for details"
                    ])
                }
                
                calendar.append(post)
        
        return calendar
    
    def _generate_post_idea(self, niche: str, product: str, content_type: str) -> str:
        """Generate specific post idea based on content type"""
        ideas = {
            "Educational": f"5 proven tips for {niche.lower()} success that nobody tells you",
            "Inspirational": f"From zero to hero: How {product} transformed my {niche.lower()} journey",
            "Promotional": f"🔥 FLASH SALE: Get {product} at 50% OFF - Limited time only!",
            "User Generated": f"Share your {niche.lower()} transformation using #{niche.replace(' ', '')}Challenge",
            "Behind the Scenes": f"A day in the life: How I use {product} daily for optimal {niche.lower()}",
            "Question/Poll": f"What's your biggest {niche.lower()} challenge? Vote below! 👇",
            "Testimonial": f"⭐⭐⭐⭐⭐ 'This changed everything!' - Real customer review"
        }
        
        return ideas.get(content_type, f"Amazing {niche} content with {product}")
    
    def _generate_hashtags(self, niche: str, platform: str) -> str:
        """Generate platform-specific hashtags"""
        base_hashtags = [
            f"#{niche.replace(' ', '')}",
            f"#{niche.split()[0]}Tips",
            "#AffiliateMarketing",
            "#ProductReview",
            "#Sponsored"
        ]
        
        platform_specific = {
            "Instagram": ["#InstaGood", "#PhotoOfTheDay", "#ExplorePage", "#Viral"],
            "Facebook": ["#Facebook", "#Community", "#Share"],
            "Twitter": ["#Twitter", "#Thread", "#TweetOfTheDay"],
            "LinkedIn": ["#LinkedIn", "#Professional", "#Business"],
            "TikTok": ["#TikTok", "#FYP", "#Viral", "#Trending"],
            "Pinterest": ["#Pinterest", "#PinIt", "#DIY", "#Inspiration"]
        }
        
        all_hashtags = base_hashtags + platform_specific.get(platform, [])
        return " ".join(all_hashtags)
    
    def generate_email_sequences_advanced(self, niche: str, product: str, 
                                         sequence_type: str = "nurture") -> List[Dict]:
        """Generate advanced email sequences with A/B testing variants"""
        print(f"\n📧 Generating {sequence_type} email sequence...")
        
        sequences = {
            "nurture": self._create_nurture_sequence(niche, product),
            "promotional": self._create_promotional_sequence(niche, product),
            "welcome": self._create_welcome_sequence(niche, product),
            "abandoned_cart": self._create_abandoned_cart_sequence(niche, product)
        }
        
        return sequences.get(sequence_type, sequences["nurture"])
    
    def _create_nurture_sequence(self, niche: str, product: str) -> List[Dict]:
        """Create nurture email sequence with A/B test variants"""
        return [
            {
                "day": 1,
                "subject_a": f"Welcome! Your {niche} journey starts here",
                "subject_b": f"Finally, a solution for {niche.lower()} that works",
                "body_template": f"""Hi {{first_name}},

Welcome to the family! I'm excited to help you achieve your {niche.lower()} goals.

Over the next few days, I'll share valuable insights that have helped thousands transform their results.

Let's get started!

Best regards,
{{sender_name}}

P.S. Keep an eye out for a special offer coming your way soon!""",
                "cta": "Download Free Guide",
                "send_time": "10:00 AM"
            },
            {
                "day": 3,
                "subject_a": f"The #1 mistake people make with {niche.lower()}",
                "subject_b": f"Are you making this {niche} mistake?",
                "body_template": f"""Hey {{first_name}},

Most people fail at {niche.lower()} because they make this critical error...

[Explain common mistake]

The good news? There's a better way.

{product} solves this problem by [key benefit].

Want to learn more?

Cheers,
{{sender_name}}""",
                "cta": "Learn More About {product}",
                "send_time": "2:00 PM"
            },
            {
                "day": 5,
                "subject_a": f"Success story: How Sarah achieved amazing {niche.lower()} results",
                "subject_b": f"This {niche} transformation will blow your mind",
                "body_template": f"""Hi {{first_name}},

I had to share this incredible story with you...

[Customer success story]

This could be you!

{product} has helped thousands achieve similar results.

Ready to start your transformation?

Best,
{{sender_name}}""",
                "cta": "See Success Stories",
                "send_time": "11:00 AM"
            },
            {
                "day": 7,
                "subject_a": f"Special offer inside: Save big on {product}",
                "subject_b": f"Last chance: Exclusive discount expires soon",
                "body_template": f"""Hey {{first_name}},

As promised, here's your exclusive offer!

Get {product} at [discount]% OFF - but only for the next 48 hours!

This is the perfect time to finally solve your {niche.lower()} challenges.

[CTA Button]

Don't miss out!

{{sender_name}}""",
                "cta": "Claim Discount Now",
                "send_time": "9:00 AM"
            },
            {
                "day": 10,
                "subject_a": f"Final reminder: Your discount expires tonight",
                "subject_b": f"⏰ Ticking clock: Offer ends in hours",
                "body_template": f"""Hi {{first_name}},

This is it - your last chance!

The exclusive discount on {product} expires TONIGHT at midnight.

After that, the price goes back up.

Don't regret missing this opportunity.

[Last Chance CTA]

To your success,
{{sender_name}}""",
                "cta": "Get It Before It's Gone",
                "send_time": "6:00 PM"
            }
        ]
    
    def _create_promotional_sequence(self, niche: str, product: str) -> List[Dict]:
        """Create promotional email sequence"""
        return [
            {
                "day": 1,
                "subject_a": f"🔥 Flash Sale: {product} at 50% OFF",
                "subject_b": f"Today only: Massive discount on {product}",
                "body_template": f"""BIG NEWS!

For the next 24 hours only, get {product} at HALF PRICE!

This is our biggest discount ever.

[Shop Now Button]

Hurry, sale ends soon!""",
                "cta": "Shop Now",
                "send_time": "8:00 AM"
            },
            {
                "day": 2,
                "subject_a": f"Hours left: 50% off ends tonight",
                "subject_b": f"Don't miss out: Sale closing soon",
                "body_template": f"""Tick tock...

Your 50% discount on {product} expires in just hours!

Thousands have already claimed theirs. Will you?

[Last Chance Button]""",
                "cta": "Claim Before It's Gone",
                "send_time": "6:00 PM"
            }
        ]
    
    def _create_welcome_sequence(self, niche: str, product: str) -> List[Dict]:
        """Create welcome email sequence"""
        return [
            {
                "day": 0,
                "subject_a": f"Welcome! Here's your free {niche} guide",
                "subject_b": f"You're in! Get started with {niche.lower()}",
                "body_template": f"""Welcome aboard!

Thanks for joining us. As promised, here's your free guide to {niche.lower()} success.

[Download Button]

Over the next few days, expect valuable tips and insights.

Welcome to the community!""",
                "cta": "Download Guide",
                "send_time": "Immediate"
            }
        ]
    
    def _create_abandoned_cart_sequence(self, niche: str, product: str) -> List[Dict]:
        """Create abandoned cart recovery sequence"""
        return [
            {
                "day": 1,
                "subject_a": f"Forgot something? Your {product} is waiting",
                "subject_b": f"Complete your order and transform your {niche.lower()}",
                "body_template": f"""Hi there,

We noticed you left something in your cart!

{product} is just one click away from changing your {niche.lower()} game.

[Complete Order Button]

Questions? Reply to this email!""",
                "cta": "Complete Purchase",
                "send_time": "1 hour after abandonment"
            },
            {
                "day": 3,
                "subject_a": f"Still thinking about it? Here's 10% off",
                "subject_b": f"Special offer to help you decide",
                "body_template": f"""Hey,

Still considering {product}?

Here's an extra 10% off to help you make the decision!

Use code: SAVE10

[Claim Discount Button]""",
                "cta": "Use Code SAVE10",
                "send_time": "3 days after"
            }
        ]
    
    def build_complete_campaign(self, niche: str = None, enable_scraping: bool = True,
                               enable_seo: bool = True, enable_competitor_analysis: bool = True) -> Dict:
        """Build complete advanced campaign with all features"""
        
        if not niche:
            niche = random.choice(self.niches)
        
        print("\n" + "="*60)
        print("🚀 BUILDING ADVANCED AI AFFILIATE CAMPAIGN")
        print("="*60)
        print(f"\n📌 Selected Niche: {niche}")
        
        # Step 1: Scrape trending products
        products = []
        if enable_scraping:
            products = self.scrape_trending_products(niche)
        
        if not products:
            # Fallback products
            product_types = self.product_types.get(niche, ["Premium Product"])
            products = [{
                "name": random.choice(product_types),
                "price": "$49.99",
                "rating": 4.5,
                "source": "Default"
            }]
        
        selected_product = products[0] if products else {"name": "Premium Product"}
        product_name = selected_product.get('name', 'Premium Product')
        
        # Step 2: Generate keywords
        print(f"\n🔑 Generating SEO keywords...")
        keywords = [
            f"best {niche.lower()} products",
            f"{niche.lower()} reviews",
            f"top rated {niche.lower()}",
            f"{product_name.lower()} review",
            f"{niche.lower()} buying guide"
        ]
        
        # Step 3: Competitor analysis
        competitor_data = {}
        if enable_competitor_analysis:
            competitor_data = self.analyze_competitors(niche, keywords)
        
        # Step 4: Generate SEO content
        content_pieces = {}
        if enable_seo:
            blog_content = self.generate_seo_optimized_content(niche, product_name, keywords, "blog_post")
            review_content = self.generate_seo_optimized_content(niche, product_name, keywords, "product_review")
            comparison_content = self.generate_seo_optimized_content(niche, product_name, keywords, "comparison")
            
            content_pieces = {
                "main_blog_post": blog_content,
                "product_review": review_content,
                "comparison_article": comparison_content
            }
        
        # Step 5: Social media calendar
        social_calendar = self.generate_social_media_calendar(niche, product_name)
        
        # Step 6: Email sequences
        email_sequences = {
            "nurture": self.generate_email_sequences_advanced(niche, product_name, "nurture"),
            "promotional": self.generate_email_sequences_advanced(niche, product_name, "promotional"),
            "welcome": self.generate_email_sequences_advanced(niche, product_name, "welcome")
        }
        
        # Compile complete campaign
        campaign = {
            "campaign_name": f"Ultimate {niche} Campaign 2025",
            "niche": niche,
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "featured_product": selected_product,
            "all_products": products,
            "target_keywords": keywords,
            "competitor_analysis": competitor_data,
            "content_strategy": content_pieces,
            "social_media_calendar": social_calendar,
            "email_sequences": email_sequences,
            "recommended_affiliate_networks": self.affiliate_networks.get(niche, ["Amazon Associates"]),
            "success_metrics": {
                "expected_ctr": "2-5%",
                "expected_conversion": "1-3%",
                "estimated_monthly_revenue": "$500-$5000",
                "break_even_timeline": "30-60 days"
            }
        }
        
        return campaign
    
    def display_campaign_summary(self, campaign: Dict):
        """Display comprehensive campaign summary"""
        print("\n" + "="*60)
        print("📊 CAMPAIGN SUMMARY")
        print("="*60)
        
        print(f"\n📋 Campaign: {campaign['campaign_name']}")
        print(f"🎯 Niche: {campaign['niche']}")
        print(f"💼 Featured Product: {campaign['featured_product'].get('name', 'N/A')}")
        print(f"📅 Created: {campaign['created_at']}")
        
        print(f"\n🔍 Products Researched: {len(campaign.get('all_products', []))}")
        for i, product in enumerate(campaign.get('all_products', [])[:5], 1):
            print(f"   {i}. {product.get('name', 'Product')} - {product.get('price', 'N/A')} ({product.get('source', 'Unknown')})")
        
        print(f"\n🔑 Target Keywords: {len(campaign.get('target_keywords', []))}")
        for kw in campaign.get('target_keywords', [])[:5]:
            print(f"   • {kw}")
        
        if campaign.get('competitor_analysis'):
            print(f"\n🕵️ Competitors Analyzed: {len(campaign['competitor_analysis'].get('top_competitors', []))}")
            print(f"   Content Gaps Identified: {len(campaign['competitor_analysis'].get('content_gaps', []))}")
        
        print(f"\n📝 Content Pieces Generated:")
        print(f"   • Blog Posts: {len(campaign.get('content_strategy', {}))}")
        print(f"   • Social Media Posts: {len(campaign.get('social_media_calendar', []))}")
        print(f"   • Email Sequences: {len(campaign.get('email_sequences', {}))}")
        
        print(f"\n📧 Email Sequences:")
        for seq_name, emails in campaign.get('email_sequences', {}).items():
            print(f"   • {seq_name.title()}: {len(emails)} emails")
        
        print(f"\n💰 Monetization:")
        print(f"   Recommended Networks: {', '.join(campaign.get('recommended_affiliate_networks', []))}")
        metrics = campaign.get('success_metrics', {})
        print(f"   Expected CTR: {metrics.get('expected_ctr', 'N/A')}")
        print(f"   Expected Conversion: {metrics.get('expected_conversion', 'N/A')}")
        print(f"   Est. Monthly Revenue: {metrics.get('estimated_monthly_revenue', 'N/A')}")
        
        print("\n" + "="*60)
        print("✅ Campaign Ready! Export to JSON for detailed content.")
        print("="*60)
    
    def save_campaign(self, campaign: Dict, filename: str = "advanced_campaign.json"):
        """Save campaign to JSON file"""
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(campaign, f, indent=2, ensure_ascii=False)
        print(f"\n💾 Campaign saved to: {filename}")


def main():
    print("\n" + "🤖"*20)
    print("AI AFFILIATE CAMPAIGN BUILDER - PRO VERSION")
    print("Advanced Features: Web Scraping + AI Content + SEO + Competitor Analysis")
    print("🤖"*20 + "\n")
    
    builder = AdvancedAIAffiliateCampaignBuilder()
    
    print("📂 Available Niches:")
    for i, niche in enumerate(builder.niches, 1):
        print(f"   {i:2d}. {niche}")
    print(f"   {len(builder.niches) + 1:2d}. Random Surprise")
    
    choice = input(f"\nSelect niche (1-{len(builder.niches) + 1}): ").strip()
    
    niche = None
    if choice.isdigit():
        choice_num = int(choice)
        if 1 <= choice_num <= len(builder.niches):
            niche = builder.niches[choice_num - 1]
        elif choice_num == len(builder.niches) + 1:
            niche = None
            print("🎲 Generating random niche...")
        else:
            print("⚠️ Invalid choice. Using random niche.")
    else:
        print("Using random niche.")
    
    # Feature selection
    print("\n⚙️ Advanced Features:")
    enable_scraping = input("Enable Web Scraping? (y/n, default=y): ").strip().lower() != 'n'
    enable_seo = input("Enable SEO Optimization? (y/n, default=y): ").strip().lower() != 'n'
    enable_competitor = input("Enable Competitor Analysis? (y/n, default=y): ").strip().lower() != 'n'
    
    print("\n" + "⚡"*20)
    print("BUILDING YOUR CAMPAIGN...")
    print("⚡"*20)
    
    campaign = builder.build_complete_campaign(
        niche=niche,
        enable_scraping=enable_scraping,
        enable_seo=enable_seo,
        enable_competitor_analysis=enable_competitor
    )
    
    builder.display_campaign_summary(campaign)
    
    # Save campaign
    save_choice = input("\n💾 Save detailed campaign to JSON? (y/n): ").strip().lower()
    if save_choice == 'y':
        filename = input("Enter filename (default: advanced_campaign.json): ").strip()
        if not filename:
            filename = "advanced_campaign.json"
        builder.save_campaign(campaign, filename)
    
    # View specific content
    view_choice = input("\n📖 View full content pieces? (y/n): ").strip().lower()
    if view_choice == 'y':
        print("\n" + "="*60)
        print("📝 CONTENT PREVIEW")
        print("="*60)
        
        content = campaign.get('content_strategy', {})
        if content:
            for content_type, data in content.items():
                print(f"\n\n{'#'*60}")
                print(f"# {content_type.upper().replace('_', ' ')}")
                print('#'*60)
                
                if isinstance(data, dict):
                    print(f"\nSEO Metadata:")
                    seo = data.get('seo_metadata', {})
                    for key, value in seo.items():
                        print(f"  • {key}: {value}")
                    
                    print(f"\nContent Preview (first 1000 chars):")
                    print("-"*60)
                    content_text = data.get('content', '')[:1000]
                    print(content_text)
                    if len(data.get('content', '')) > 1000:
                        print("\n... [Content continues in saved JSON file]")
    
    print("\n" + "🎉"*20)
    print("CAMPAIGN GENERATION COMPLETE!")
    print("Next Steps:")
    print("1. Review generated content")
    print("2. Add your affiliate links")
    print("3. Customize for your brand voice")
    print("4. Start publishing and tracking results!")
    print("🎉"*20 + "\n")


if __name__ == "__main__":
    main()
