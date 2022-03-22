from django.http.response import HttpResponse
from django.shortcuts import render
from blog.models import Blog

#liste 
data = {
    "blogs": [
        {
            "id":1,
            "title":"Supervised Learning",
            "image":"supervised.png",
            "is_active":True,
            "is_home":True,
            "description":"Supervised learning is the types of machine learning in which machines are trained using well 'labelled' training data, and on basis of that data, machines predict the output. The labelled data means some input data is already tagged with the correct output.",
            "content":"Lorem ipsum dolor sit amet consectetur adipisicing elit. Enim consectetur suscipit error iste animi, quisquam officia itaque quidem et quasi sit assumenda earum libero! Molestias, vel magnam. Itaque eum laudantium doloremque exercitationem culpa obcaecati, soluta quam distinctio illum ex officia asperiores necessitatibus debitis? Omnis doloremque reprehenderit amet dicta fuga voluptatum deleniti fugit, minima ipsum nostrum aut, perferendis vel officiis suscipit molestiae saepe id eos obcaecati impedit possimus nisi nobis perspiciatis aliquam? Nisi vitae repudiandae commodi, maxime ea temporibus magnam iure perferendis pariatur provident, placeat, ullam delectus omnis ducimus. Omnis ut, odit debitis consequuntur exercitationem sequi itaque asperiores dicta. Ea, assumenda. Sit facere quod soluta suscipit temporibus porro perspiciatis dolorem ratione, saepe aspernatur officiis nulla nihil? Distinctio ex in repellat libero doloribus ab quaerat dolore dolores obcaecati modi rem sit consectetur numquam iure, non porro totam, deleniti beatae perspiciatis amet repudiandae, quos consequatur? Distinctio dolore libero molestias harum repellendus ipsum eaque temporibus vel culpa error numquam, odio ratione fugiat odit voluptatibus, accusantium rem labore modi nisi cum deleniti iste ipsam asperiores reiciendis. Commodi at autem, molestiae soluta consectetur adipisci ea sed dicta error quisquam sequi ut cum ullam rem minima doloremque, officiis culpa sit magni enim. Molestias tempore ipsam dolorem rerum, accusamus officia voluptatibus nulla delectus saepe suscipit consectetur ab! Dolorum ratione minima quia hic at facere, distinctio eveniet esse suscipit nobis impedit deserunt eaque ex. Reprehenderit, quis. Dolores eum possimus explicabo amet eaque sit corporis quasi! Voluptatibus cupiditate distinctio nesciunt placeat! Mollitia magnam unde sequi voluptatibus dolore, expedita architecto deleniti a, blanditiis aliquid quas accusamus tempora consequatur vitae velit vel cum culpa praesentium deserunt nesciunt voluptatem! Libero consequatur fugit possimus itaque, delectus aspernatur. Rerum, aliquam dolor quia neque magni pariatur sapiente hic vel laborum voluptatibus ad cupiditate suscipit quae, ab animi ut amet quis ipsum recusandae repudiandae, nisi sequi rem! Quae aspernatur fuga quam laboriosam ab perferendis hic quos voluptas vero voluptate rerum enim, necessitatibus recusandae fugiat obcaecati delectus dolor consequuntur sed! Non deserunt fuga assumenda culpa maxime cum recusandae perferendis consequatur blanditiis maiores nesciunt quaerat dolorum libero, deleniti eum alias quae ratione dolore a provident nihil. Autem consectetur sit cum, doloremque quas dignissimos, tenetur sed alias harum animi temporibus aperiam fuga numquam nisi mollitia maxime amet, eius est commodi quia sunt id quae a? Repellendus possimus voluptatem, itaque, accusamus quos deleniti rerum provident fugiat a ratione debitis unde ab, nulla in consequatur. Adipisci earum impedit repellat quod quos quas eius qui tempora eaque pariatur. Mollitia laborum sed ut velit, ipsam hic obcaecati, at provident placeat magni nemo atque quas aperiam tempore expedita numquam consequatur rem ullam quasi, reiciendis impedit quo quibusdam quidem! Dignissimos, ipsa, voluptatibus est quasi facilis alias hic voluptatem aperiam atque pariatur porro aliquid maxime cumque quibusdam odit itaque ad minima delectus deserunt distinctio quos! Quasi atque vitae hic praesentium accusantium numquam provident doloremque. Recusandae ipsum a sunt ea accusamus corrupti dignissimos enim accusantium velit officia eveniet soluta quam magnam, voluptas, qui laboriosam expedita, minima at. Odit quibusdam maxime voluptatibus nihil eius est rerum nemo iste ducimus!"
        },
        {
            "id":2,
            "title":"Unsupervised Learning",
            "image":"unsupervised.png",
            "is_active":True,
            "is_home":True,
            "description":"In the previous topic, we learned supervised machine learning in which models are trained using labeled data under the supervision of training data. But there may be many cases in which we do not have labeled data and need to find the hidden patterns from the given dataset. So, to solve such types of cases in machine learning, we need unsupervised learning techniques.",
            "content":"Lorem ipsum dolor sit amet consectetur adipisicing elit. Enim consectetur suscipit error iste animi, quisquam officia itaque quidem et quasi sit assumenda earum libero! Molestias, vel magnam. Itaque eum laudantium doloremque exercitationem culpa obcaecati, soluta quam distinctio illum ex officia asperiores necessitatibus debitis? Omnis doloremque reprehenderit amet dicta fuga voluptatum deleniti fugit, minima ipsum nostrum aut, perferendis vel officiis suscipit molestiae saepe id eos obcaecati impedit possimus nisi nobis perspiciatis aliquam? Nisi vitae repudiandae commodi, maxime ea temporibus magnam iure perferendis pariatur provident, placeat, ullam delectus omnis ducimus. Omnis ut, odit debitis consequuntur exercitationem sequi itaque asperiores dicta. Ea, assumenda. Sit facere quod soluta suscipit temporibus porro perspiciatis dolorem ratione, saepe aspernatur officiis nulla nihil? Distinctio ex in repellat libero doloribus ab quaerat dolore dolores obcaecati modi rem sit consectetur numquam iure, non porro totam, deleniti beatae perspiciatis amet repudiandae, quos consequatur? Distinctio dolore libero molestias harum repellendus ipsum eaque temporibus vel culpa error numquam, odio ratione fugiat odit voluptatibus, accusantium rem labore modi nisi cum deleniti iste ipsam asperiores reiciendis. Commodi at autem, molestiae soluta consectetur adipisci ea sed dicta error quisquam sequi ut cum ullam rem minima doloremque, officiis culpa sit magni enim. Molestias tempore ipsam dolorem rerum, accusamus officia voluptatibus nulla delectus saepe suscipit consectetur ab! Dolorum ratione minima quia hic at facere, distinctio eveniet esse suscipit nobis impedit deserunt eaque ex. Reprehenderit, quis. Dolores eum possimus explicabo amet eaque sit corporis quasi! Voluptatibus cupiditate distinctio nesciunt placeat! Mollitia magnam unde sequi voluptatibus dolore, expedita architecto deleniti a, blanditiis aliquid quas accusamus tempora consequatur vitae velit vel cum culpa praesentium deserunt nesciunt voluptatem! Libero consequatur fugit possimus itaque, delectus aspernatur. Rerum, aliquam dolor quia neque magni pariatur sapiente hic vel laborum voluptatibus ad cupiditate suscipit quae, ab animi ut amet quis ipsum recusandae repudiandae, nisi sequi rem! Quae aspernatur fuga quam laboriosam ab perferendis hic quos voluptas vero voluptate rerum enim, necessitatibus recusandae fugiat obcaecati delectus dolor consequuntur sed! Non deserunt fuga assumenda culpa maxime cum recusandae perferendis consequatur blanditiis maiores nesciunt quaerat dolorum libero, deleniti eum alias quae ratione dolore a provident nihil. Autem consectetur sit cum, doloremque quas dignissimos, tenetur sed alias harum animi temporibus aperiam fuga numquam nisi mollitia maxime amet, eius est commodi quia sunt id quae a? Repellendus possimus voluptatem, itaque, accusamus quos deleniti rerum provident fugiat a ratione debitis unde ab, nulla in consequatur. Adipisci earum impedit repellat quod quos quas eius qui tempora eaque pariatur. Mollitia laborum sed ut velit, ipsam hic obcaecati, at provident placeat magni nemo atque quas aperiam tempore expedita numquam consequatur rem ullam quasi, reiciendis impedit quo quibusdam quidem! Dignissimos, ipsa, voluptatibus est quasi facilis alias hic voluptatem aperiam atque pariatur porro aliquid maxime cumque quibusdam odit itaque ad minima delectus deserunt distinctio quos! Quasi atque vitae hic praesentium accusantium numquam provident doloremque. Recusandae ipsum a sunt ea accusamus corrupti dignissimos enim accusantium velit officia eveniet soluta quam magnam, voluptas, qui laboriosam expedita, minima at. Odit quibusdam maxime voluptatibus nihil eius est rerum nemo iste ducimus!"
        },
        {
            "id":3,
            "title":"Reinforcement Learning",
            "image":"reinforcement.jpg",
            "is_active":True,
            "is_home":False,
            "description":"Reinforcement Learning is a feedback-based Machine learning technique in which an agent learns to behave in an environment by performing the actions and seeing the results of actions. For each good action, the agent gets positive feedback, and for each bad action, the agent gets negative feedback or penalty.",
            "content":"Lorem ipsum dolor sit amet consectetur adipisicing elit. Enim consectetur suscipit error iste animi, quisquam officia itaque quidem et quasi sit assumenda earum libero! Molestias, vel magnam. Itaque eum laudantium doloremque exercitationem culpa obcaecati, soluta quam distinctio illum ex officia asperiores necessitatibus debitis? Omnis doloremque reprehenderit amet dicta fuga voluptatum deleniti fugit, minima ipsum nostrum aut, perferendis vel officiis suscipit molestiae saepe id eos obcaecati impedit possimus nisi nobis perspiciatis aliquam? Nisi vitae repudiandae commodi, maxime ea temporibus magnam iure perferendis pariatur provident, placeat, ullam delectus omnis ducimus. Omnis ut, odit debitis consequuntur exercitationem sequi itaque asperiores dicta. Ea, assumenda. Sit facere quod soluta suscipit temporibus porro perspiciatis dolorem ratione, saepe aspernatur officiis nulla nihil? Distinctio ex in repellat libero doloribus ab quaerat dolore dolores obcaecati modi rem sit consectetur numquam iure, non porro totam, deleniti beatae perspiciatis amet repudiandae, quos consequatur? Distinctio dolore libero molestias harum repellendus ipsum eaque temporibus vel culpa error numquam, odio ratione fugiat odit voluptatibus, accusantium rem labore modi nisi cum deleniti iste ipsam asperiores reiciendis. Commodi at autem, molestiae soluta consectetur adipisci ea sed dicta error quisquam sequi ut cum ullam rem minima doloremque, officiis culpa sit magni enim. Molestias tempore ipsam dolorem rerum, accusamus officia voluptatibus nulla delectus saepe suscipit consectetur ab! Dolorum ratione minima quia hic at facere, distinctio eveniet esse suscipit nobis impedit deserunt eaque ex. Reprehenderit, quis. Dolores eum possimus explicabo amet eaque sit corporis quasi! Voluptatibus cupiditate distinctio nesciunt placeat! Mollitia magnam unde sequi voluptatibus dolore, expedita architecto deleniti a, blanditiis aliquid quas accusamus tempora consequatur vitae velit vel cum culpa praesentium deserunt nesciunt voluptatem! Libero consequatur fugit possimus itaque, delectus aspernatur. Rerum, aliquam dolor quia neque magni pariatur sapiente hic vel laborum voluptatibus ad cupiditate suscipit quae, ab animi ut amet quis ipsum recusandae repudiandae, nisi sequi rem! Quae aspernatur fuga quam laboriosam ab perferendis hic quos voluptas vero voluptate rerum enim, necessitatibus recusandae fugiat obcaecati delectus dolor consequuntur sed! Non deserunt fuga assumenda culpa maxime cum recusandae perferendis consequatur blanditiis maiores nesciunt quaerat dolorum libero, deleniti eum alias quae ratione dolore a provident nihil. Autem consectetur sit cum, doloremque quas dignissimos, tenetur sed alias harum animi temporibus aperiam fuga numquam nisi mollitia maxime amet, eius est commodi quia sunt id quae a? Repellendus possimus voluptatem, itaque, accusamus quos deleniti rerum provident fugiat a ratione debitis unde ab, nulla in consequatur. Adipisci earum impedit repellat quod quos quas eius qui tempora eaque pariatur. Mollitia laborum sed ut velit, ipsam hic obcaecati, at provident placeat magni nemo atque quas aperiam tempore expedita numquam consequatur rem ullam quasi, reiciendis impedit quo quibusdam quidem! Dignissimos, ipsa, voluptatibus est quasi facilis alias hic voluptatem aperiam atque pariatur porro aliquid maxime cumque quibusdam odit itaque ad minima delectus deserunt distinctio quos! Quasi atque vitae hic praesentium accusantium numquam provident doloremque. Recusandae ipsum a sunt ea accusamus corrupti dignissimos enim accusantium velit officia eveniet soluta quam magnam, voluptas, qui laboriosam expedita, minima at. Odit quibusdam maxime voluptatibus nihil eius est rerum nemo iste ducimus!"
        }
    ] #veritabanından gelen veriler gibi düşünelim
}

#veritabanı
data = {
    'blogs': Blog.objects.all()
}#alternatif 1 

blogs_data = Blog.objects.all()#alternatif 2


def index(request):
    context = {
        #"blogs":data["blogs"] #liste veya alternatif 1 için
        #'blogs': blogs_data.filter(is_home = True) # html de if ile yapmadıysak burada filter ile true olanları gösteririz
        'blogs': blogs_data
    }
    return render(request, "blog/index.html", context)

def blogs(request):
    context = {
        #"blogs":data["blogs"]
        #"blogs": blogs_data
        'blogs': blogs_data.filter(is_active = True)
    }
    return render(request, "blog/blogs.html", context)

def blog_details(request, id):
    #blogs = data["blogs"]

    # selected_blog = None

    #alternatif 1
    # for blog in blogs:
    #     if blog['id'] == id:
    #         selected_blog = blog

    #alternatif 2
    #selectedBlog = [blog for blog in blogs if blog.id==id][0] 
    # #blog['id'] yerine blog.id yazdık çünkü obje olrak dönen parametreye ulaşırız veya kısa yol olarak filter kullanırız

    #alternatif 3
    #selectedBlog = blogs_data.filter(id =id)[0]
    
    selectedBlog = blogs_data.get(id = id)


    return render(request, "blog/blog-details.html", {
        "blog": selectedBlog
    })