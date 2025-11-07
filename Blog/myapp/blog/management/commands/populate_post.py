from blog.models import Post
from django.core.management.base import BaseCommand



class Command(BaseCommand):
    
    help = "This command inserts Post data"

    def handle(self, *args, **options):
        titles = [
            "10 Blog Topics That Will Skyrocket Your Traffic in 2025",
            "Top 20 Blogging Trends to Watch in 2025",
            "7 Inspiring and New Trending Blog Post Ideas for 2025",
            "5 Ways to Use AI for Daily Productivity",
            "How to Build a Personal Brand in the AI Era",
            "What Will Social Media Look Like in 2030?",
            "Why I Quit My Job to Travel the World with a Drone",
            "ChatGPT vs Gemini: Which AI Assistant Wins in 2025?",
        ]

        contents = [
            "Discover the hottest blog topics that are driving massive engagement and clicks this year.",
            "Stay ahead of the curve with these must-know blogging trends shaping the digital landscape.",
            "Fresh, creative blog post ideas to captivate your audience and keep your content calendar full.",
            "Learn how AI tools can streamline your workflow and supercharge your everyday efficiency.",
            "Craft a standout personal brand that thrives in a world dominated by artificial intelligence.",
            "A bold look into the future of social platforms, from immersive tech to AI-driven interactions.",
            "A personal journey of freedom, creativity, and capturing the globe from breathtaking new heights.",
            "A head-to-head comparison of the top AI assistants—features, performance, and who comes out on top.",
        ]

        image_urls = [
            "https://picsum.photos/id/1/800/400",
            "https://picsum.photos/id/10/800/400",
            "https://picsum.photos/id/2/800/400",
            "https://picsum.photos/id/20/800/400",
            "https://picsum.photos/id/3/800/400",
            "https://picsum.photos/id/30/800/400",
            "https://picsum.photos/id/4/800/400",
            "https://picsum.photos/id/40/800/400",
        ]

        for title, content, image_url in zip(titles, contents, image_urls):
            Post.objects.create(title=title, content=content, image_url=image_url)

        self.stdout.write(self.style.SUCCESS("Inserting Data Successfully Completed"))