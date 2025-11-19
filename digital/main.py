import streamlit as st
import pathlib
import base64
import datetime


# Set the page configuration
st.set_page_config(page_title='My Website', layout='wide')

# Sidebar navigation
page = st.sidebar.radio('Navigation',
                        ['🏠 Introduction', '🌱 Analysis', '😊 Interaction', '💖 About Us'],
                        key='main_nav')

if page == '🏠 Introduction':
    st.image("image/introduction/Cover1.0.jpg", use_container_width=True) 
    st.title("🎭 Constructing the Image of 关羽 in Peking Opera")


    st.write('''
    关羽, as a historical figure from the Three Kingdoms period, has long been regarded in Chinese traditional culture as the embodiment of 忠义 (loyalty and righteousness).  
    He is not only remembered as a heroic character in historical narratives but has also been continuously reshaped and reproduced in folk beliefs, literary works, and the operatic stage.  
    However, this image is not immutable; it has been reconstructed across different historical periods and scripts.  
    With the development of digital humanities methods, we can now employ text mining, network analysis, and visualization techniques to systematically reveal 关羽’s role positioning and cultural significance in Peking Opera scripts.
    ''')

    # Core Research Question
    st.header('❓ Core Research Question')
    st.subheader('🔎 Main Question')
    st.write('''
    How is 关羽 in Peking Opera scripts constructed as the archetypal figure of 忠义  
    through the multiple dimensions of linguistic style, character relationships, narrative function, and cultural symbolism?  
    ''')


    # Research Objectives
    st.header('🎯 Research Objectives')
    st.subheader('📚 Academic Significance')
    st.write('''
    To uncover the mechanisms by which 关羽’s image is constructed in Peking Opera scripts through digital methods,  
    thereby enriching scholarly perspectives on the study of traditional operatic characters.  
    ''')

    st.subheader('🛠 Methodological Innovation')
    st.write('''
    To integrate text analysis, network analysis, and visualization techniques,  
    exploring new pathways for applying digital humanities to the study of Chinese opera.  

    ''')

    st.subheader('🌏 Cultural Value')
    st.write('''
    To interpret the process by which 关羽’s 忠义 image is symbolized in stage art,  
    reflecting its enduring place within Chinese cultural memory and value systems.  
    ''')

    # Methodology Preview
    st.header('🔮 Methodology Preview')

    st.subheader('📝 Linguistic Style Analysis')
    st.write('''
    By applying word frequency statistics, keyword extraction, and sentiment analysis,  
    we can reveal the solemn, forceful, and concise features of 关羽’s lines.  
    His language often emphasizes terms related to 忠, 义, and 勇, highlighting his moral character.  
    Comparing his style with other characters allows us to trace how his image evolves across scripts and contexts.  
    ''')

    st.subheader('🤝 Character Relationship Analysis')
    st.write('''
    By constructing co-occurrence networks, we can visualize 关羽’s interactions with 刘备, 张飞, 曹操 and others,  
    and measure his centrality in the narrative.  
    This helps explain how relational dynamics contribute to his positioning as the embodiment of 忠义.  
    ''')

    st.subheader('📖 Narrative Function Analysis')
    st.write('''
    Using narratological frameworks, we can identify 关羽’s functions:  
    as an agent of plot progression, a moral symbol, or a source of conflict.  
    Segmenting scripts into narrative nodes reveals whether his functions remain consistent or vary across plays.  
    ''')

    st.subheader('🎨 Cultural Symbolism Analysis')
    st.write('''
    关羽 is also a cultural icon. His red face symbolizes loyalty and righteousness,  
    the 青龙偃月刀 represents martial power, and temple worship reinforces his deification.  
    Extracting symbolic terms and imagery shows how 关羽 is staged as a cultural symbol of 忠义.  

    ''')

    # Data Sources
    st.header('📂 Data Sources')
    st.write('''
    - **中国京剧戏考网** ([https://scripts.xikao.com/](https://scripts.xikao.com/)):  
      A comprehensive digital archive of 京剧 scripts, containing over 1100 plays and 1500+ script versions.  
      收录自2000年以来的京剧剧本，目前已包含 1162 出剧目、1578 出剧本，是最系统的京剧剧本数字化数据库之一。  

    - **国立传统艺术中心 (Taiwan)** ([http://www.ncfta.gov.tw/cp.aspx?n=1784](http://www.ncfta.gov.tw/cp.aspx?n=1784)):  
      Provides digitized resources on traditional opera, including costumes, stage performance archives, and cultural artifacts.  
      提供京剧服饰、表演艺术与相关档案的数字化资源，涵盖舞台服装、行头、化妆等文化符号信息。
    ''')

    # Expected Outcomes
    st.header('🌟 Expected Outcomes')
    st.write('''
    - **Visualizations**: word clouds, relationship networks, narrative timelines, symbolic imagery maps.  
    - **Scholarly Contribution**: a multidimensional framework for analyzing operatic characters using digital humanities.  
    - **Cultural Insight**: deeper understanding of how 忠义 is embodied and transmitted through the figure of 关羽 in Peking Opera.  
    ''')


elif page == '🌱 Analysis':

    st.image("image/introduction/Cover1.0.jpg", use_container_width=True)

    st.title('🌱 Deep Dives into GuanYu in Peking Opera')

    # Sub-navigation for the "Analysis " page
    Analysis_page = st.sidebar.radio('Analysis Sections',
                                  ['Scripts Analysis','Character Positioning Analysis', 'Guanyu role orientation and personality','Cultural symbols and images'],
                                  key='plant_nav')
    if Analysis_page == 'Character Positioning Analysis':
        st.header("Character Positioning Analysis of Guan Yu")

        # 1. Top 20 Interactions
        st.subheader("Top 20 Interactions with Guan Yu")
        st.write("""
              This “Top 20 Interactions with Guan Yu” bar chart reveals Guan Yu's role association network by counting how frequently other characters mention him in their lines.
           - Liu Bei (380 times), Zhuge Liang (338 times), and Cao Cao (288 times) rank the top three, highlighting Guan Yu's dual core status in **the core power layer of Shu Han** (Liu Bei is his sworn brother and monarch, Zhuge Liang is his strategic partner) and **the top-tier camp of Cao Wei** (Cao Cao is a powerful enemy who appreciates him). He is a key anchor in the narrative of Shu Han's regime and an important link in the military and political game between Wei and Shu in the Three Kingdoms period.
           - The high-frequency mentions of generals like Zhang Liao and Huang Zhong (both over 70 times) reflect Guan Yu's influence as a “benchmark general” among military colleagues and opponents. His military achievements and decisions are the focus of military narratives from all parties.
           - The mentions of Ma Tong, Zhou Cang, and Guan Ping (relatives/attendants) show the multi-dimensionality of Guan Yu's role—he is not only a battlefield hero but also a leader with family ties and followers. The existence of his personal team strengthens the daily-life support for his image of “unparalleled loyalty”.""")
        st.image("image/Character/output1.png")

        # 2. Aliases vs Roles Bubble Chart
        st.subheader("Bubble Chart of Guan Yu’s Aliases vs Top 20 Roles")
        st.write("""
              This “Bubble Chart of Guan Yu’s Aliases vs Top 20 Roles” reveals the intimacy of role relationships and differences in identity cognition by counting the frequency of different characters addressing Guan Yu by his aliases.
             - **Kinship/Core Group Dimension**: The alias “Er Di (Second Brother)” appears frequently in the lines of Liu Bei and Zhuge Liang, reflecting the intimate address within Shu Han’s core circle (sworn brothers and strategic partners) and highlighting Guan Yu’s dual identity as “brother + general” in Shu Han’s power structure. “Yun Chang” and “Guan Mou” are frequently used by characters like Liu Bei and Cao Cao, serving as formal or self-referential addresses among acquaintances or opponents, reflecting Guan Yu’s identity switching in personal relationships and military games.
             - **Honorific Dimension**: The occasional mentions of “Guan Jiangjun (General Guan)” and “Guan Gong” reflect the recognition of his military identity by the Cao Wei and Eastern Wu camps, which are honorific titles based on his military reputation. The use of “Hanshou Tinghou” is associated with his official title, reflecting the importance some characters attach to his political identity.
             - **Cultural Symbol Dimension**: The distribution of different aliases also reflects the diversity of Guan Yu’s image—he is both “Er Di” and “Yun Chang” in Shu Han (a personified brother/general) and a military symbol respected as “Jiangjun” and “Gong” by all parties in the Three Kingdoms context. His alias system is a composite mirror of role relationships and social identities.""")
        st.image("image/Character/output2.png")

        # 3. Aliases vs Camps Bubble Chart
        st.subheader("Aliases in Different Camps")
        st.write("""
              This bubble chart “Frequency of Guan Yu’s Appellations in the Camps of Wei, Shu, Wu, and Other Warlords” reveals the differences in role relationships and identity cognition between various camps and Guan Yu through the frequency of using his aliases in different camps.
             - **Shu Camp**: The prominent bubbles of “Er Di (Second Brother)” and “Yun Chang” reflect the intimate addresses from core members like Liu Bei and Zhang Fei to Guan Yu, representing the emotional and identity binding in the sworn brotherhood and the core circle of Shu Han, highlighting his dual role as “family member + core general” in Shu Han.
             - **Wei Camp**: The high frequency of formal appellations such as “General Guan” and “Guan Yun Chang” reflects that the Wei camp regards Guan Yu as a military opponent, using official and formal addresses to reflect the recognition of his general identity and the identity definition in the game.
             - **Wu and Other Warlords Camps**: The distribution of appellations like “Guan Gong” and “Hanshou Tinghou” reflects the attention to Guan Yu’s military reputation and political identity, which is the external cognition of his identity as “famous general + feudal lord” under the game pattern of the Three Kingdoms.""")
        st.image("image/Character/output3.jpg")

        # 4. Interaction Network
        st.subheader("Guan Yu Interaction Network Diagram")
        st.write("""
              This “Guan Yu Interaction Network Diagram” takes Guan Yu as the core, intuitively presenting his complex role relationship network.
            1. Core Circle: Nodes like Liu Bei, Zhang Fei, and Zhuge Liang have thick edges and prominent nodes with Guan Yu, reflecting the deep binding of the core group of Shu Han. Their intimate interactions as sworn brothers, monarch and minister, and partners form the foundation of Guan Yu’s image of “unparalleled loyalty” and “loyalty to the monarch”.
             2. Military Opponent Circle: Nodes such as Cao Cao, Zhang Liao, and Pang De and their edges with Guan Yu reflect military games, which are key interactions in the military conflict between Wei and Shu in the Three Kingdoms period, highlighting Guan Yu’s core position as a general on the battlefield.
            3. Peripheral Association Circle: Although peripheral nodes like grooms and garrison soldiers have low interaction frequency, they complement the multiple facets of Guan Yu’s life and battlefield as a “person”, showing that he is not only a hero but also in the interaction network of ordinary roles.""")
        st.image("image/Character/output4.png")

        # 5. Word Clouds of Four Camps
        st.subheader("Word Clouds of Four Camps")
        st.write("""
              This “Word Cloud of Four Camps” reveals the role cognition and relationship logic of Guan Yu in different camps through the visual differences of keyword frequencies.
           - **Shu Camp**: Keywords such as “Di (Brother)”, “Mei (Beautiful)”, “Cao Cao”, and “Taoyuan” are prominent. “Di” reflects the brotherhood in the core circle of Shu Han, “Taoyuan” is associated with the sworn brotherhood foundation, and “Cao Cao” is the main military opponent. It reflects that Guan Yu has the dual roles of “brother-general” and “anti-Wei vanguard” in Shu Han, and his image is deeply bound to the emotional ties and strategic confrontation of Shu Han.
           - **Wei Camp**: Keywords such as “Yun Chang”, “Guan Gong”, “General”, and “Yan Liang” are significant. “Yun Chang” and “Guan Gong” are honorific titles for his general identity, “Yan Liang” is associated with his classic battle achievement, and “Prime Minister (Cao Cao)” reflects the Wei camp’s attention to military games with him. It shows that the Wei camp regards Guan Yu as a powerful military opponent, and its cognition focuses on his military value and military interaction between Wei and Shu.
           - **Wu Camp**: Keywords such as “Guan Gong”, “Jingzhou”, “Cao Cao”, and “Lu Meng” are prominent. “Jingzhou” is the focus of geopolitical competition, and “Lu Meng” is a key figure in Dong Wu’s game. It reflects that Guan Yu is recognized as “the core opponent in Jingzhou game” in the Wu camp, and his role is associated with Dong Wu’s geopolitical strategy and military checks and balances.
           - **Other Warlords Camp**: Keywords such as “Yun Chang”, “Liu Bei”, “Taoyuan”, and “Hua Xiong” are dominant. “Hua Xiong” is a symbol of his early famous battle, and “Liu Bei” and “Taoyuan” are his identity background. It shows that the cognition of Guan Yu in other warlords camp tends to be “early famous general + Shu Han symbol”, which is a symbolic cognition based on pan-military narrative and identity labels.""")
        st.image("image/Character/output5.png")

        # 6. Line Chart of Top 10 High-Frequency Words
        st.subheader("Top 10 High-Frequency Words in Four Camps")
        st.write("""
           This “Line Chart with Area Fill for Top 10 High-Frequency Words in Four Camps” reveals the differences in role cognition and relationships of Guan Yu among various camps through the distribution of high-frequency vocabulary mentioning Guan Yu in different camps.
           - **Shu Camp**: High-frequency words such as “Mou Jia (I)”, “Er Di (Second Brother)”, and “San Di (Third Brother)” are prominent, reflecting the intimate addresses from the core circle of Shu Han (Liu Bei, Zhang Fei, etc.) to Guan Yu. It reflects his dual role as “sworn brother + core general of Shu Han” and is an intimate role association based on family-like emotions and regime binding.
           - **Wei Camp**: High-frequency words such as “Yun Chang”, “Guan Gong”, and “Mei Ran (Beautiful Beard)” dominate, reflecting that the Wei camp regards Guan Yu as a famous military general and opponent. Formal and prestigious addresses highlight his identity as a general, which is a role cognition based on military games.
           - **Wu Camp**: The high-frequency words imply geopolitical conflicts (such as the context related to Jingzhou) and military confrontation logic, reflecting that Dong Wu regards Guan Yu as an external opponent in strategic games, and the role association focuses on geopolitical competition and military checks and balances.
           - **Other Warlords Camp**: The high-frequency words are low in frequency and scattered, reflecting that other warlords have less interaction with Guan Yu, and their cognition of him tends to be a symbolic “general” image. The role association is weak, mostly based on rumors or generalized military symbol cognition.""")
        st.image("image/Character/output6.png")

        # 7. Guan Yu Mentions Other Generals
        st.subheader("Generals Mentioned in Guan Yu’s Lines (Top 15)")
        st.write("""
           This “Line Chart with Area Fill of Other Generals Mentioned in Guan Yu’s Lines (Top 15)” reveals Guan Yu’s role focus and relationship network through the frequency of his active mentions of other generals.
          - **Core Strategic Circle of Shu Han**: Zhuge Liang (over 300 times) and Liu Bei (250 times) rank in the top two, reflecting Guan Yu’s dual core attention to Shu Han’s “strategic advisor” and “monarch brother”. It directly embodies his role positioning of “loyalty to the monarch and assistance in governance + brotherly coordination”, reflecting his interactive logic of coordinating strategic decisions with military actions and supporting political stability with brotherly friendship in the Shu Han regime.
          - **Core Military Opponents in Game**: The high-frequency mentions of Cao Cao (over 130 times) and Zhang Liao (50 times) highlight Guan Yu’s military attention to the top-tier camp of Cao Wei (leader + key general) as a general. It is a microcosm of the “general vs. general, general vs. lord” game pattern in the military conflict between Wei and Shu, embodying the focal association of his general identity in military confrontation.
          - **Personal Force and Subordinate Circle**: The mentions of Ma Tong, Guan Ping, Zhou Cang, etc., show Guan Yu’s management and dependence on his personal team as a general, which is an extension of his “battlefield leader” identity in daily life, reflecting his command and trust relationship with subordinates in military operations.""")
        st.image("image/Character/output7.png")

        # 8. Guan Yu’s Words to Liu Bei, Zhang Fei, Zhuge Liang
        st.subheader("High-Frequency Words in Guan Yu’s Lines to Liu Bei, Zhang Fei, Zhuge Liang")
        st.write("""
           This “Line Chart with Area Fill for Top 10 High-Frequency Words in Four Camps” reveals the role cognition and relationship logic of Guan Yu in different camps through the distribution of high-frequency vocabulary mentioning Guan Yu.
          - **Shu Camp**: High-frequency words such as “Guan Mou (I)”, “Er Di (Second Brother)”, “San Di (Third Brother)”, and “Cao Cao” are prominent. “Guan Mou” reflects Guan Yu’s self-identity in Shu Han; “Er Di” and “San Di” are intimate addresses from core members like Liu Bei and Zhang Fei, highlighting the emotional binding of the sworn brotherhood circle in Shu Han; “Cao Cao” as the main military opponent indicates Guan Yu’s role as an “anti-Wei vanguard” from the perspective of Shu Han, whose image deeply integrates the emotional ties and strategic confrontation of Shu Han.
          - **Wei Camp**: High-frequency words such as “Yun Chang”, “Guan Gong”, “Lao Fu (Old Man)”, and “Cheng Xiang (Prime Minister)” are significant. “Yun Chang” and “Guan Gong” are honorific titles for his general identity, reflecting the Wei camp’s recognition of his military value; the high-frequency mention of “Cheng Xiang (Cao Cao)” reflects that the Wei camp regards Guan Yu as a core military opponent, with cognition focusing on the confrontation in the military game between Wei and Shu.
          - **Wu Camp**: High-frequency words such as “Guan Gong”, “Jingzhou”, “Cao Cao”, and “Zhu Gong (Lord)” are prominent. “Jingzhou” is the focus of geopolitical competition between Wu and Shu, and the mention of “Guan Gong” is deeply bound to the Jingzhou game, reflecting that Dong Wu regards Guan Yu as a key opponent in geopolitical strategy, whose role is associated with Dong Wu’s political ambition and military checks and balances.
          - **Other Warlords Camp**: High-frequency words such as “Liu Bei”, “Zu Fu (Grandfather)”, and “Guan Yun Chang” are low in frequency and scattered. “Liu Bei” and “Zu Fu” reflect the other warlords’ cognition of Guan Yu’s background as “Shu Han general + family identity”; “Guan Yun Chang” is a generalized general symbol, indicating that the other warlords’ cognition of Guan Yu tends to be an early famous general label, with less interaction and symbolic characteristics.""")
        st.image("image/Character/output8.png")
    elif Analysis_page == 'Cultural symbols and images':
        st.header('Cultural symbols and images')
        symbol_cover_photo_path = "./image/1.PNG"
        st.image(symbol_cover_photo_path, width=500)

        st.subheader(
            "In Peking Opera, Guan Yu\'s cultural symbols form a rigorous and self-consistent system: Core symbols define who he is (忠义勇武).\n Secondary symbols specifically demonstrate how he upheld these virtues through stories, objects, and titles.\n Derived imagery, through poetic rendering, tells the audience the aesthetic and spiritual heights reached by his loyalty, righteousness, courage, and martial prowess.\n Loyalty, Righteousness, Courage, and Martial Prowess are the four pillars of Guan Yu\'s cultural symbol, underpinning all his stories and imagery.")

        st.subheader('1. 忠 Loyalty ')
        st.write(
            'It is mainly reflected in "staying in Cao Ying but with his heart loyal to Han" and "resigning his post and returning the gold seals". Cao Cao offered him high official positions and generous rewards, but once he learned of Liu Bei\'s whereabouts, he resolutely abandoned all glory and wealth to return to his former lord. This absolute loyalty to his sworn brother and the imperial power of the Han Dynasty is the most noble political virtue in Confucian thought.')
        st.markdown("---")

        st.subheader('2. 义 Righteousness ')
        st.write(
            'This is the core of Guan Yu\'s personal charm. It is embodied in "sparing Cao Cao out of righteousness at Huarong Trail". To repay Cao Cao\'s kindness in the past, he risked military punishment to let his powerful enemy escape. This difficult choice and final decision between "personal righteousness" and "public loyalty" elevated Guan Yu\'s image from a mere military general to a moral paragon who values friendship and keeps his promises, with flesh and blood.')
        st.markdown("---")

        st.subheader('3. 勇武 Courage and Martial Prowess ')
        st.write(
            'These are the military guarantees for the realization of his "loyalty" and "righteousness". A series of allusions such as "attending the meeting with a single sword", "crossing five passes and slaying six generals", and "beheading Hua Xiong while the wine was still warm" repeatedly strengthen his image as an unparalleled and invincible super warrior.')
        st.markdown("---")

        st.subheader('4. The Relationship Between the Four Core Symbols ')
        st.write(
            '"Martial Prowess" is the foundation, "Courage" is the temperament, "Loyalty" is the direction, and "Righteousness" is the soul. He had the ability (martial prowess) and courage to fulfill his promises, and his actions were always guided by the highest moral principles of "loyalty" and "righteousness".')

        title1 = "1. Allusion Symbols: Specific Narratives of \"Loyalty, Righteousness, Courage, and Martial Prowess\""
        st.markdown(f"<h4 style='text-align: left; font-size:24px;'>{title1}</h4>", unsafe_allow_html=True)
        list1 = [
            ("Loyalty Dimension",
             '''- The Oath of the Peach Garden (brotherly loyalty) \n- staying in Cao Ying with his heart loyal to Han (loyalty to the Han Dynasty) \n- resigning his post and returning the gold seals (abstaining from wealth to uphold loyalty).'''),
            ("Righteousness Dimension",
             '''- Sparing Cao Cao out of righteousness at Huarong Trail (righteousness of repaying kindness) \n- beheading Cai Yang at the Meeting of the Ancient City (righteousness of vindicating his brother) '''),
            ("Courage and Martial Prowess Dimension",
             '''- Beheading Hua Xiong while the wine was still warm \n- crossing five passes and slaying six generals \n- beheading Yan Liang and Zhu Wenchou (unrivaled martial skill on the battlefield) \n- attending the meeting with a single sword (courage in venturing alone into danger)'''),
            ("Tragic Undertone",
             '''- Defeat and flight to Maicheng (the hero's downfall, completing his image).'''),
        ]

        # 创建多列
        cols = st.columns(4)  # 根据需要调整列数

        for col, (title, content) in zip(cols, list1):
            with col:
                # 使用更小号的标题字体
                st.markdown(f"<h4 style='text-align: center; font-size:18px;'>{title}</h4>", unsafe_allow_html=True)
                st.write(content)
        st.markdown("---")

        title2 = "2. Object Symbols: Visual Markers"
        st.markdown(f"<h4 style='text-align: left; font-size:24px;'>{title2}</h4>", unsafe_allow_html=True)
        cols = st.columns(3)
        with cols[0]:
            st.info("🗡️ **青龙偃月刀**\n- Symbol of martial prowess\n- Bound to Guan Yu's bravery")
        with cols[1]:
            st.success("🐎 **赤兔马**\n- Speed and nobility\n- Justifies 'five passes, six generals'")
        with cols[2]:
            st.warning("👕 **青袍**\n- Iconic costume\n- Strengthens audience memory")

        st.markdown("---")
        title3 = "3. Identity Symbols: Endorsements of Authority and Legitimacy"
        st.markdown(f"<h4 style='text-align: left; font-size:24px;'>{title3}</h4>", unsafe_allow_html=True)
        st.info(
            "🧑 **关云长**: Personal identity recognition, core title among people and stage.\n\n📜 **汉寿亭侯**: Official title, legitimacy and authority, echoing loyalty to Han.")
        st.markdown("---")

        title4 = "4. Scene Imagery: Creating Atmosphere and Reflecting Mood"
        st.markdown(f"<h4 style='text-align: left; font-size:24px;'>{title4}</h4>", unsafe_allow_html=True)
        st.success(
            "🌊 **大江**: Corresponding to scenes like the \"single sword meeting\". \n It highlights the hero's broad and heroic spirit.\n\n🏯 **麦城**: Linked to \"defeat and flight to Maicheng\". \n It evokes a tragic atmosphere and adds tension to the hero's image.\n\n⛰️ **土山**: Associated with the \"Three Agreements on Earth Mountain\" \n It reflects Guan Yu's dilemma and choices in upholding loyalty and righteousness.")
        st.markdown("---")

        title5 = "5. Behavioral Imagery: Highlighting Character and Sentiment"
        st.markdown(f"<h4 style='text-align: left; font-size:24px;'>{title5}</h4>", unsafe_allow_html=True)
        st.warning(""" 
               **夜读《春秋》**: Shows that Guan Yu "was a warrior with literary grace", highlighting his elegance and perseverance beyond loyalty and righteousness. \n
               **封金舍袍**: Refusing wealth in Cao Cao's camp, reinforcing his character of "being loyal to his former lord and not coveting fame and fortune". \n
               **温酒斩华雄**: Condenses his martial traits, becoming a classic scene of "速胜" and "神威".
           """)
        st.markdown("---")

        title6 = "6. Emotional Imagery: Emotional Expressions of the Spiritual Core"
        st.markdown(f"<h4 style='text-align: left; font-size:24px;'>{title6}</h4>", unsafe_allow_html=True)
        st.error(
            "❤️ **丹心**: Corresponding to loyalty, it is the spiritual portrayal of \"身在曹营心在汉\".\n\n🔥 **豪气**: Corresponding to courage, martial prowess, and righteousness, embodied in scenes like the \"单刀会\" and \"过五关斩六将\".\n\n🩸 **英雄血**: Linked to \"败走麦城\", it is both the end of the tragedy and a symbol of martyrdom for the spirit of loyalty and righteousness.")
    elif Analysis_page == 'Guanyu role orientation and personality':
        st.header("Guan Yu's Role Orientation and Personality Analysis")

        # First, Guan Yu's role orientation and personality
        st.subheader("1. Core Role Positioning")
        st.write('''
* Military leader: As an important general under Liu Bei, Guan Yu plays a central role in military operations, responsible for directing operations and formulating strategies. According to statistics, this is Guan Yu's most important functional orientation, with a frequency of 130 times.
* Protector: Guan Yu often undertakes the responsibility of protecting Liu Bei and his family, showing his loyalty and sense of responsibility. This function is particularly prominent in classic plots such as "riding a thousand miles alone".
* Moral model: Guan Yu was portrayed as the embodiment of loyalty, and his words and deeds became the standard of moral judgment in the play.
* Key decision-makers: At many critical moments, Guan Yu's decisions have a great impact on the plot, such as "Huarong Daoyi explained Cao Cao" and other plots.
* Conflict promoter: Guan Yu's personality and behavior often trigger or solve conflicts in the play and push the story forward.
        ''')
        st.image("Guanyu_anaylize/1_guanyu_character_development.png")

        st.subheader("2. Personality Characteristics")
        st.write('''
* Loyalty and righteousness: This is Guan Yu's most prominent personality characteristic (frequency of appearance 150 times). Guan Yu's loyalty to Liu Bei and his attention to the feeling of loyalty constitute the core of his character.
* Bravery: Guan Yu, as a fierce general, is invincible on the battlefield, and the plot of beheading Yan Liang and killing Wen Chou highlights this feature.
* Empathy: Guan Yu shows complex and profound affection towards Liu Bei, Zhang Fei, and even Cao Cao, which enriches the emotional level of the role.
* Calm: At critical moments, Guan Yu often shows calmness and composure, and can make wise judgments.
* Arrogance: This is a negative feature of Guan Yu's personality, and it has also become one of the important reasons for his final defeat in Maicheng.
        ''')
        st.image("Guanyu_anaylize/2_guanyu_multi_dimension_analysis.png")

        # Second, the multidimensional analysis of narrative function
        st.header("Second, Multidimensional Analysis of Narrative Function")

        st.subheader("1. Plot Promotion Mechanism and Intensity")
        st.write('''
Guan Yu promoted the development of the plot through various types of events. The intensity and influence of different events are different, which can be divided into the following categories:
① Action events (25 times): Guan Yu's specific actions directly promoted the development of the plot, such as "going to the meeting with one knife" and "flooding seven armies".
② Conflict-type events (18 times): The conflict that Guan Yu participated in or triggered became a plot turning point, such as the intensification of the conflict with Soochow.
③ Decision-making events (15 times): Guan Yu's key decisions changed the plot direction, such as "releasing Cao Cao" and "refusing marriage".
④ Emotional events (10 times): Guan Yu's emotional expression and inner struggle enriched the plot level.
⑤ Loyalty events (7 times): Guan Yu's key moments to show loyalty, such as "riding a thousand miles alone".
        ''')
        st.write('''
Among them, "Huarong Daoyi explained Cao Cao", "Riding a Thousand Miles Alone" and "Defeating Maicheng" are the three pillar events of Guan Yu's narrative function:
① "Huarong Daoyi Interprets Cao Cao": It is an important turning point of the plot to reflect Guan Yu's character of attaching importance to affection and change the short-term pattern of the Three Kingdoms.
② "Riding alone for thousands of miles": highlighting his loyalty and bravery, and laying the dual position of his moral model and military leader;
③ "Defeating Maicheng": It marks the end of Guan Yu's tragic fate, sublimates the theme of "loyalty and righteousness" and arouses readers' emotional resonance.
        ''')
        st.image("Guanyu_anaylize/3_guanyu_event_types.png")
        st.image("Guanyu_anaylize/4_guanyu_plot_driving_trend.png")
        st.image("Guanyu_anaylize/5_guanyu_character_network.png")

        st.subheader("2. Dynamic Evolution of Functions")
        st.write('''
Guan Yu's narrative function is dynamically adjusted with the change of story stage, showing a clear evolution track:
① Early rising stage (Taoyuan became sworn-warm wine killed Hua Xiong): The core function is "role shaping" (score 90 points). The loyalty background is established through the loyalty in Taoyuan, and Hua Xiong is displayed with warm wine, thus the basic image of Guan Yu's loyalty and bravery is quickly established.
② Peak stage (riding alone for thousands of miles-flooding seven armies): the core functions are transformed into "plot turning" (score 95 points) and "conflict escalation" (score 90 points). Riding a thousand miles to promote the reunion of Liu Bei Group, Huarong Daoyi explained Cao Cao's fate, flooded the Seventh Army to reach the peak of military achievements, and intensified the conflict with Soochow, which became the key to accelerate the development of the plot.
③ Crisis stage (careless loss of Jingzhou-trapped in Maicheng): the core function is changed to "emotional rendering" (score 90 points). After Jingzhou fell, Guan Yu fell from the peak, and his anxiety and remorse paved the way for the tragic ending.
④ Tragedy ending stage (failure in Maicheng-physical death): the core functions are upgraded to "theme deepening" (score 95 points) and "emotional rendering" (score 100 points). Guan Yu's death is not only the end of personal fate, but also sublimates the theme of "loyalty" in the book and becomes one of the most emotional fragments.
        ''')

        # Third, the analysis of social relations
        st.header("Third, Analysis of Social Relations")
        st.write('''
Guan Yu's social network connects different camps, and the intensity of its interaction with the main characters directly affects the plot development and role shaping, which can be divided into two categories: allies and opponents:
Major allies:
① Liu Bei: The interaction frequency is the highest and the relationship is the closest, which is the core link of Taoyuan. The deep brotherhood between them is the core source of Guan Yu's "loyalty and righteousness" character. Many decisions of Guan Yu (such as finding a brother thousands of miles away) revolve around Liu Bei, which affects the development direction of Liu Bei Group.
② Zhang Fei: As sworn brothers, there are both battlefield cooperation and personality conflicts. The interaction between them enriches the role relationship within Liu Bei Group and enhances the authenticity of the narrative.
③ Zhuge Liang: There were strategic differences in the early stage, and gradually became strategic partners in the later stage. Zhuge Liang's strategy of "uniting with Wu to resist Cao" is in contrast with Guan Yu's tough attitude, and their interaction directly affects Jingzhou's strategic decision.
④ Zhao Yun: Both of them are generals under Liu Bei. They have a harmonious relationship and often work together in the battlefield. The interaction between them highlights the unity within Liu Bei Group and strengthens the group characteristics of "loyalty and righteousness"
Main opponent:
① Cao Cao: The most complicated opponent, with both hostility and respect, constitutes an important emotional conflict in the narrative and enriches the versatility of the role.
② Sun Quan: The contradiction intensified because of Guan Yu's arrogance. The opposition between the two men directly triggered the war in Jingzhou, which was an important inducement of Guan Yu's tragic fate.
③ Lv Meng: Guan Yu's key opponent, who ultimately led to his downfall, made a surprise attack on Jingzhou through "crossing the river in white". It is the concentrated explosion point of the contradiction between Dongwu and Liubei Group.
④ Zhou Yu: Battle of Red Cliffs's main rival before and after laid the groundwork for the subsequent Jingzhou dispute.
        ''')
        st.image("Guanyu_anaylize/12_guanyu_narrative_heatmap.png")

        # Fourth, the chart analysis summary
        st.header("Fourth, Chart Analysis Summary")
        st.write('''
This study quantitatively analyzes Guan Yu's narrative function from multiple dimensions through visual charts, and the core charts are interpreted as follows.
1. The frequency of Guan Yu's appearance in the main scripts: "Riding alone for a thousand miles" (221 times), "Walking in Maicheng" (180 times) and "One-knife Meeting" (115 times) are the highest, which reflects his key position in the core plot and confirms the importance of the "Three Pillars Event".
2. Distribution of Guan Yu's behavior types (pie chart): Military action (34.8%) and combat (24.6%) account for more than 50%, highlighting the core attributes of his military commanders; The proportion of decision-making (17.4%), conversation (13.0%) and emotional expression (10.2%) is relatively low, which is in line with his calm and quiet personality.
3. The radar chart of Guan Yu's personality characteristics: loyalty (100 points) and bravery (95 points) are the highest dimensions, and arrogance (40 points) is the lowest dimension, which intuitively presents the core advantages and fatal defects of his personality.
4. Histogram of Guan Yu's function orientation: Military leaders (130 times) appear most frequently, followed by protectors (100 times), moral models (95 times), conflict promoters (85 times) and key decision makers (75 times).
5. Analysis of the intensity of interaction network between Guan Yu and the main characters: Liu Bei (95 points), Zhang Fei (90 points) and Cao Cao (85 points) are the top three, which confirms the core node of Guan Yu's social network and reflects its pivotal role in connecting different camps.
        ''')
        st.image("Guanyu_anaylize/7_guanyu_play_frequency.png")
        st.image("Guanyu_anaylize/8_guanyu_behavior_distribution.png")
        st.image("Guanyu_anaylize/9_guanyu_character_radar.png")
        st.image("Guanyu_anaylize/10_guanyu_function_analysis.png")
        st.image("Guanyu_anaylize/11_guanyu_character_interactions.png")

        # Fifth, the comprehensive evaluation of Guan Yu's narrative function
        st.header("Fifth, Comprehensive Evaluation of Guan Yu's Narrative Function")
        st.subheader("1. Positioning of Core Narrative Function")
        st.write('''
① Plot turning point: Key actions (such as Huarong's release of Cao and the flooding of the Seventh Army) have repeatedly become the nodes of plot turning, pushing the story from one stage to the next.
② Theme bearer: It is the only core carrier and concrete embodiment of the theme of "loyalty and righteousness"
③ Conflict engine: It is not only the initiator of external conflict, but also the resolver of internal conflict, providing tension for narrative.
④ Role relationship hub: Its social network covers the main forces of the three countries, and promotes the intertwined development of multiple plots through interaction.
⑤ Emotional resonance point: The fate track from peak to tragedy stimulates readers' value recognition and enhances the artistic appeal of the works.
        ''')
        st.image("Guanyu_anaylize/12_guanyu_narrative_heatmap.png")

        st.subheader("2. Uniqueness of Narrative Function")
        st.write('''
① Multifunctional: It undertakes multiple functions such as plot promotion, theme expression and emotional rendering at the same time, avoiding the limitations of a single functional role.
② Penetration: From the beginning of the story, Taoyuan became righteous, to the peak battle in the middle period, and then to the tragic ending in the later period, its narrative function runs through the book, and it is one of the few characters who accompany the complete development process of Liu Bei Group.
③ Persistence of influence: Its key decisions can have a far-reaching impact across the story stage. For example, Huarong's release of Cao Cao and the Northern Expedition of Fancheng not only affect the current plot, but also have a far-reaching impact on the plots in subsequent stages.
④ Emotional depth: The versatility of personality and emotional complexity make the role more realistic and infectious.
        ''')
        st.image("Guanyu_anaylize/13_guanyu_driving_types_statistics 2.png")
        st.image("Guanyu_anaylize/14_guanyu_driving_types_statistics.png")
        st.image("Guanyu_anaylize/6_guanyu_narrative_efficiency.png")

        # Sixth, Research conclusions
        st.header("Sixth, Research Conclusions")
        st.subheader("(A) Main Findings")
        st.write('''
* Role complexity: Guan Yu is a three-dimensional role with multiple orientations and complex personality, which is the root of his eternal artistic charm.
* Core plot driving force: Guan Yu's behavior and decision-making directly affect the key trend of the narrative of the Three Kingdoms, and the three pillar events constitute an important plot node of the book.
* Cultural symbolic meaning: Beyond the category of literary role, it has become synonymous with the spirit of "loyalty and righteousness" in traditional culture.
* Dialectical relationship between character and fate: Loyalty and bravery made him a hero, while arrogance led to his tragic ending, full of profound tragic beauty.
        ''')
        st.subheader("(B) Theoretical Significance")
        st.write('''
* Through Guan Yu's case, the narrative theories such as "diversity of role functions" and "dynamic evolution of functions" are verified, which provides concrete samples for the analysis of literary role functions.''')
    elif Analysis_page == 'Scripts Analysis':
        st.header("Scripts Analysis of Guan Yu in Peking Opera")
        st.header("Linguistic Style and Personality Background")
        st.write("""

            As one of the most renowned generals of the Three Kingdoms, Guan Yu is traditionally portrayed with a “red-faced” heroic image in Peking Opera.
            This study extracts his lines from multiple scripts and analyzes word frequency, high-frequency terms, and sentiment orientation,
            in order to investigate his linguistic style and symbolic representation.

            Based on text-mining results, Guan Yu appears as a figure whose speech embodies loyalty, righteousness, steadfastness,
            and a solemn personality core. His emotional tendencies reflect his hierarchical status and moral position.
            """)
        st.header(" 1. High-Frequency Vocabulary")
        st.image("image/Scripts/1.png")
        st.image("image/Scripts/2.png")
        st.write("""
            Among all terms used by Guan Yu, 255 high-frequency words are identified. Many reveal his irreplaceable emotional and social position.

            Common high-frequency relational terms include:
            • “Eldest brother (大哥)” (122)
            • “Sir (先生)” (120)
            • “Younger brother (贤弟)” (112)
            • “Fourth brother (四弟)” (95)
            • “Second brother (二位)” (88)
            • “Elder brother (兄长)” (70)
            • “Princess / Lady of the palace (皇嫂)” (50)
            • “Second sister-in-law (二嫂)” (46)

            These words construct a dense relational and kinship network, centered around sworn brotherhood and royal ties.

            Guan Yu repeatedly uses respectful forms of address, demonstrating clear hierarchical order, deep fraternal affection,
            and strict moral propriety. His language reveals a personality that values etiquette, discipline, and unwavering loyalty.

            A second cluster of high-frequency terms comes from self-referential address such as:
            • “I, Guan Yunchang (关某)” (123)
            • “This one (某)” (656)

            These forms emphasize humility yet dignity, reflecting his noble identity.

            By contrast, terms involving antagonists — such as Cao Cao (104), rebels (奸) (61), and traitors (逆) (47) — constitute another lexical group.
            This set reflects:
            • Guan Yu’s unwavering sense of justice,
            • His moral stance against treachery,
            • His ultimate conflict with adversaries.

            Guan Yu’s linguistic world is therefore built upon loyalty to brothers, allegiance to righteousness, and moral resistance to wrongdoing.
            Even in conversations with enemies, he maintains clarity of role and responsibility, expressing stable emotional control and a clear worldview.
            """)

        st.subheader("2. Variety in Vocal Techniques")
        st.image("image/Scripts/6.png")
        st.write("""
           Across the scripts analyzed, Guan Yu’s singing style uses a wide range of techniques:

           • Heavy, stately vocal lines to establish authority  
           • Powerful resonance in central sections  
           • Western-style falsetto (82 occurrences) to express inner sorrow  
           • Short and forceful tones (52 occurrences) for dramatic tension

           These choices give his vocal performance an ancient, dignified color, befitting a sacred, disciplined, and ritualized martial figure.
           He is presented not as a reckless warrior but as a solemn, graceful leader.

           The Xiangyan Index calculated as 1.4821 shows that his vocal style possesses moderate-to-high diversity.
           He does not rely on a single pattern but adjusts his vocal techniques flexibly according to dramatic context.

           Bright tones such as:
           • “White-tone chanting” (25)
           • “Baritone resonance” (40)
           • “Open-throat declamation” (218)
           • “Nasal chanting” (108)

           all appear frequently, revealing rich variation and emotional depth.

           These stylistic choices highlight:
           • his calm dignity,
           • ritualized authority,
           • and steady self-possession.

           During climactic scenes, Guan Yu demonstrates restrained anger, moral judgment, and awe-inspiring presence through vocal shifts between
           falsetto, chest voice, scattered tones, fast declamation, and various rhythmic transitions.

           Techniques such as:
           • “Western-style falsetto” (47)
           • “Dispersed tones”
           • “Fast rhymed chanting” (28)

           are used in scenes involving:
           • confrontation,
           • battle readiness,
           • moral reasoning,
           • righteous indignation.

           These techniques strengthen his image as a heroic, fierce, yet morally upright general,
           giving his performances remarkable dramatic power.
           """)

        st.subheader("3. Personality and Emotional Traits")
        st.write("""
          Guan Yu’s emotional core centers on loyalty:
          • loyalty to his sworn elder brother (Liu Bei),
          • loyalty to Zhang Fei,
          • loyalty to the royal widow (the two imperial ladies).

          Loyalty is his emotional anchor stone.

          His pride and confidence appear through frequent self-references and defiant attitudes toward Cao Cao, Sun Quan,
          and other opposing forces. These expressions show the deep-rooted pride of a heroic figure conscious of his own righteousness.

          The fierce, heroic traits are further supported by high-frequency words associated with:
          • warhorses,
          • Cao Cao,
          • battle,
          • anger,
          • martial action verbs.

          Combined with impassioned singing techniques, these terms construct the dramatic persona of a first-rank warrior among the “Ten Thousand Troops.”
          """)

        st.subheader("4. Emotional Structure Based on a Classical Chinese Sentiment Lexicon")
        st.image("image/Scripts/5.png")
        st.image("image/Scripts/3.png")
        st.write("""
        Using a custom Classical Chinese sentiment lexicon, all of Guan Yu’s lines are annotated and scored.
        The results reveal a clear three-layer emotional structure:

        • High-positive zone (≥ 0.7): dominated by commendatory terms and strong positive verbs such as “loyalty”, “righteousness”,
          “virtue”, “prestige”, “bravery”. These lines appear in oaths, declarations of stance, and expressions of responsibility,
          constructing his image as a moral exemplar and “Martial Sage of Loyalty and Righteousness”.
        • Neutral zone (0.4–0.6): made up of descriptive, judgmental, and command lines used to assess the situation, deploy troops,
          and discuss strategies. The tone is calm and restrained, highlighting his rational, steady side as a commander.
        • Low-emotion zone (≤ 0.3): driven by strong negative action verbs such as “kill”, “behead”, “execute”, “capture”, “rebuke angrily”.
          These are concentrated in battle scenes and confrontations with traitors, expressing not weakness, but a heroic, righteous fury.

        Together, these layers form a stable model: loyalty and virtue at the surface, composure and self-control inside,
        and thunderous martial ferocity at the core.
        """)

        st.subheader("4. Cross-Script Consistency: A Shared Archetype of Lord Guan")
        st.image("image/Scripts/4.png")
        st.write("""
        When we compare different plays such as “Meeting at the Single Blade”, “Huarong Trail”, “Beheading Hua Xiong”,
        “Meeting at the Ancient City”, and “Battle of Changsha”, we find that:

        • High-positive lines are consistently clustered around loyalty, righteousness, and moral authority.
        • Neutral narrative and command lines show similar patterns of calm, concise, and elegant Classical Chinese across scripts.
        • Low-emotion lines are always tied to battle, denunciation of treachery, or decisive choices about life and death.

        This indicates that Guan Yu is not shaped by a single script, but by a long-term operatic tradition that repeatedly reproduces
        a shared “Lord Guan archetype”: loyalty as foundation, civil virtue as body, martial ferocity as edge, steadiness as temperament.
        """)

        st.subheader("5. Alignment with the Hongsheng Role Type")
        st.write("""
        The emotional structure above matches closely with the requirements of the Hongsheng role type in Peking Opera,
        which emphasizes majesty, dignity, firmness, and heroic intensity.

        • High-positive emotions correspond to the Hongsheng ideals of solemnity and moral nobility.
        • The large proportion of neutral, steady lines fits the vocal requirement of being calm, weighty, and restrained.
        • Concentrated low-emotion segments with “kill”, “behead”, and “anger” provide textual support for explosive moments on stage,
          where voice, rhythm, movement, and weapon routines jointly display Guan Yu’s fierce heroism.

        In this way, textual features, emotional structure, and performative conventions interlock,
        turning Guan Yu into a highly stylized yet deeply influential image of the Martial Saint in Peking Opera.
        """)





elif page == '😊 Interaction':
    cover_photo_path = "https://github.com/DMGT-0810/CHC5904/blob/8652118f2b19b34c2c20d5432b9e3be203982b72/digital/image/17.png?raw=true"
    st.image(cover_photo_path, use_column_width=True)

    st.title('😊 Interaction')
    # st.write('Here you can find information about our team and our history.')

    st.header('''1. "A Poet's Quest" Interactive Game''')
    st.write('''
    ⭐🌿 Let's Embark on a Journey Through Poetry, Plants, and Time!

    This is an interactive, educational storytelling experience where you embark on a journey as a poet. The game combines visual elements, audio, and interactive features to create a captivating experience.

    ''')

    # 定义要嵌入的网页链接
    url = "https://view.genially.com/673c89a7fffb4fdecd627489/interactive-image-a-poets-quest"
    # 使用HTML的iframe元素嵌入网页
    iframe_html = f"""
        <iframe src="{url}" width="100%" height="400" frameborder="0">
            <p>您的浏览器不支持iframe标签。</p>
        </iframe>
        """
    # 使用st.markdown展示iframe，并设置unsafe_allow_html=True允许HTML代码渲染
    st.markdown(iframe_html, unsafe_allow_html=True)
    # 添加一个链接，点击可以直接跳转到网页
    st.markdown(f"[Click here.]({url})", unsafe_allow_html=True)

    st.subheader("🔍 Navigating the Game")
    categories_content = {
        "🚀 To Start": '''After loading, click through the buttons to uncover details, click "Start" button to begin your quest.''',
        "🎮 Interactive Elements": "Look for clickable icons, buttons, or images throughout the game. These will allow you to:\n  - Uncover interesting facts about the plants\n  - Interact with objects or characters, find the key to advance the storyline\n  - You can revisit previous sections by clicking on the left button on the side of the screen",
        "🧐 Explore Thoroughly": "Click on all interactive elements to uncover hidden clues and secrets.",
        "🎁 Find the treasure!": "Complete the quest to find a hidden surpise!"
    }
    # 创建展开框显示各类别内容
    for category, content in categories_content.items():
        with st.expander(f"{category}"):
            st.write(content)

    st.header('2. “古人看花” Mini-Programme')
    st.write('''
        ✨🌸 Welcome to Our WeChat Mini Program! 

        Discover the wonders of plants like never before! 🌿 Through this mini program, you can explore new plant species 🌼, view plants from the perspective of ancient cultures 📜, and uncover the emotions and historical stories they represent 💕📖. Let's dive into the beauty of nature together! 

        Please scan the QR code below:

        ''')
    st.image('https://github.com/DMGT-0810/CHC5904/blob/8652118f2b19b34c2c20d5432b9e3be203982b72/digital/image/10.png?raw=true', width=300)

    st.subheader("🔍 User Guide")
    categories_content = {
        "📷 Scan the QR Code to Access the Mini Program": "- Use your WeChat app to scan the QR code.\n- Apply for experience permissions if required.",
        "🌿 Upload or Take a Photo of a Plant": "Once inside the Mini Program, you can either upload an existing photo of a plant or take a new one directly using your device's camera.",
        "🤖 Plant Identification with AI": "After uploading the image, the program uses Baidu's image recognition API to identify the plant species for you.",
        "📜 Discover Ancient Plant-Related Poems": "Using OpenAI's GPT-4 model, the program searches the ctext database to find two Chinese ancient poems related to the identified plant.",
        "🌸 View Results in an Easy-to-Read Format": "The program displays:\n- The plant's name.\n- The full text of the two related ancient poems.\n- The imagery and symbolism of the plant in the poems."
    }
    # 创建展开框显示各类别内容
    for category, content in categories_content.items():
        with st.expander(f"{category}"):
            st.write(content)

elif page == '💖 About Us':
    st.title('💖 About Us')
    st.subheader('✨ Team Members')
    st.write('''1.Technological Development:

    Shen Ziqi 

    Ye Haoqi 
    
    Lve Shao Han
     
    Ye Jing

                ''')
    st.write('''2.Humanities Analysis:

    XIAO Qifang (24003563G@connect.polyu.hk)

    DENG Junxuan(24043858G@connect.polyu.hk)

    ZENG Jingwen(24073054G@connect.polyu.hk)

    ZHANG Fengyue (24100774G@connect.polyu.hk)

    TIAN Yuan (24073183G@connect.polyu.hk)
            ''')

    st.subheader('🔍 Methodology')
    st.write('''1.Why we are interested in this research topic on plants, seasons, emotions and locations?

    The Book of Songs and its plant descriptions carry rich cultural connotations, representing the essence of traditional culturje. The botanical descriptions, in thwe Book of Songs contawin abundant cultural information. As carriers of emotion, plants embody the ancient people's sentiments and attitudes toward life. Meanwhile, the geographical features and seasonal climate reflected by these plants are alyso crucial components of their imagery. Analyzing the plants in thme Book of Songs through information visualizationg helps us understand its cultural messages and pass on both the Book of Songs and Chinese. 
                ''')
    st.write('''2.How we selected the plants?

    We used a text analysis tool to count the eight most frequently mentioned plants, which are: mulberry (40 times), millet (26 times), kudzu (21 times), grass (19 times), beans (11 times), pine (11 times), cypress (10 times), and bamboo (7 times).

               ''')
    st.write('''3.How do we present the content?

    We present the georaphical locations of plants through GIS, conduct close reading on seasons, emotional connotations, and human qualities, and we also created an interactive mini-game and a photo-poetry recognition mini-programme to provide users with a diverse experience.
                   ''')

    st.subheader('🎨 Workflow')
    # 滑块
    w = [
        "Occurrences of plants: \nThe Book of Songs contains 305 poems, among which 153 mention plants. Based on this data, we wrote a python program to create a pie chart for this overall distribution.",
        "Frequency of top mentioned plants: \nUsing text analysis tools, we identified the eight most frequently mentioned plants in the Book of Songs, which we then selected as our target species for further study. Subsequently, we created a bar chart to visualize this data.",
        "Emotional themes in selected plants: \nWe analyzed the emotional themes expressed through plants in the Book of Songs and categorized them into major categories and subcategories. This hierarchical structure helps understand the rich emotional palette of the poetry collection.",
        '''Emotional theme network: \nWe created a network visualization to show the relationships between plants and their associated emotional themes in the Book of Songs. The network consists of main emotional categories (like "Love & Longing", "Diligent Life", "National Spirit") connected to specific plant-emotion pairs.''',
        "Seasonal distribution: \nThe seasonal distribution of plants in the Book of Songs was analyzed in two complementary ways - a pie chart showing the overall distribution and a stacked bar chart showing the distribution by plant species. ",
        "Geographical location: \nTo perform GIS, I combined data with conclusions provided by AI to preliminarily determine the geographic locations (latitude and longitude) of the plants.",
    ]
    # 创建一个滑块
    index = st.slider(" ", 1, len(w), format="Step %d")
    st.write(w[index - 1])

    st.subheader('💻 Our Code ')
    codelink = "https://arcg.is/10COOr2"
    st.markdown(f'[<{codelink}>]({codelink})', unsafe_allow_html=True)

    st.subheader('📖 Reference')
    # 定义链接
    url1 = "http://eprints.utar.edu.my/3850/1/fyp_CH_2019_TJM_%2D_1606961.pdf"
    url3 = "https://oversea.cnki.net/KCMS/detail/detail.aspx?dbcode=CJFD&dbname=CJFDLASN2023&filename=MAZH202305010&uniplatform=OVERSEA&v=ylSE49hEQkLdQ_zny4qeAJlaWElvQap7IxdLk7zWRZlr2SeN0Ynobe8yX_fDtfrE"
    url4 = "https://oversea.cnki.net/KCMS/detail/detail.aspx?dbcode=CJFD&dbname=CJFDLAST2018&filename=YWJS201804015&uniplatform=OVERSEA&v=K9p3VYC-6rsA3W6KSAWAs0jLCWjP-buyn8UaIir4LH-gX8HxCdHCFtTe_jdqwXqm"
    url5 = "https://oversea.cnki.net/KCMS/detail/detail.aspx?dbcode=CJFD&dbname=CJFDLAST2024&filename=JGWC202443030&uniplatform=OVERSEA&v=Ey6v7oEDe65heEuSYReYV_-3EdAUGFLx6uykHfNpSLMZtITItdwvDdfG7SIooSA2"
    url6 = "https://oversea.cnki.net/KCMS/detail/detail.aspx?dbcode=CJFD&dbname=CJFDLASN2021&filename=QCSY202114025&uniplatform=OVERSEA&v=_s-ENeE-4H0QCJAmWVPg_1zUTrFs0du_rtqI2DMDzJSeVEeVeKWPGO-vwSWeqB2q"

    # showcase
    st.write(f'[1.《诗经》中“桑”的意向]({url1})')
    st.write(f'[2. 大河印象——《诗经·国风》里的河流书写与情感建构]({url3})')
    st.write(f'[3. 刻骨铭心的爱与怨——《诗经·卫风·氓》情感脉络解析]({url4})')
    st.write(f'[4.《诗经》植物信息可视化应用研究]({url5})')
    st.write(f'[5.《诗经》中的植物及其意象分析——以《诗经·国风》中的植物为例]({url6})')

    st.subheader('💎Original Text')
    url3 = "https://ctext.org/book-of-poetry"
    # 使用HTML的iframe元素嵌入网页
    iframe_html = f"""
            <iframe src="{url3}" width="100%" height="400" frameborder="0">
                <p>您的浏览器不支持iframe标签。</p>
            </iframe>
            """
    # 使用st.markdown展示iframe，并设置unsafe_allow_html=True允许HTML代码渲染
    st.markdown(iframe_html, unsafe_allow_html=True)
    # 添加一个链接，点击可以直接跳转到网页
    st.markdown(f"[Click here.]({url3})", unsafe_allow_html=True)




