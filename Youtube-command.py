@client.command()
async def yt(ctx, *, question):
  	async with aiohttp.ClientSession() as session:
    	async with session.get(f'https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=5&q={question}&key=AIzaSyDvYo8xP7OFdZr_TKMqXO1CUgqQBSEaYik') as resp:
      		js = await resp.json()
	        print(js)
	        youtube = discord.Embed(
      			title=f"Youtube Search Results For {question.capitalize()[:2] + '...'}",
            	color=0xff0000
      		)
      		description = None
      		description1 = None
      		description2 = None
      		description3 = None
      		description4 = None

		    if js['items'][0]['id']['kind'] == 'youtube#channel':
        		title = js['items'][0]['snippet']['title'][:10] + ' - Channel'
        		if len(js['items'][0]['snippet']['description']) > 29:
          			description = f"[{js['items'][0]['snippet']['description'][:20] + '...' + js['items'][0]['snippet']['publishedAt'][:8]}](https://www.youtube.com/channel/{js['items'][0]['id']['channelId']})"
        		elif len(js['items'][0]['snippet']['description']) <= 29:
          			description = f"[{js['items'][0]['snippet']['description'][:20] + ' - ' + js['items'][0]['snippet']['publishedAt'][:8]}](https://www.youtube.com/channel/{js['items'][0]['id']['channelId']})"
        		elif js['items'][0]['snippet']['description'] == '':
          			description = f"[None](https://www.youtube.com/channel/{js['items'][0]['snippet']['channelId']})"
      		elif js['items'][0]['id']['kind'] == 'youtube#video':
        		title = js['items'][0]['snippet']['title'][:8] + ' - Video'
        		if len(js['items'][0]['snippet']['description']) > 29:
          			description = f"[{js['items'][0]['snippet']['description'][:20] + '...' + js['items'][0]['snippet']['publishedAt'][:8]}](https://www.youtube.com/watch?v={js['items'][0]['id']['videoId']})"
        		elif len(js['items'][0]['snippet']['description']) <= 29:
          			description = f"[{js['items'][2]['snippet']['description'][:20] + ' - ' + js['items'][0]['snippet']['publishedAt'][8]}](https://www.youtube.com/watch?v={js['items'][0]['id']['videoId']})"
        		elif js['items'][0]['snippet']['description'] == '':
          			description = f"[None](https://www.youtube.com/watch?v={js['items'][0]['id']['videoId']})"
      		elif js['items'][0]['id']['kind'] == 'youtube#playlist':
        		title = js['items'][0]['snippet']['title'][:11] + ' - Playlist'
        		if len(js['items'][0]['snippet']['description']) > 29:
          			description = f"[{js['items'][0]['snippet']['description'][:20] + '...' + js['items'][0]['snippet']['publishedAt'][:8]}](https://www.youtube.com/watch?list={js['items'][0]['id']})"
        		elif len(js['items'][0]['snippet']['description']) <= 29:
          			description = f"[{js['items'][0]['snippet']['description'][:20] + ' - ' + js['items'][0]['snippet']['publishedAt'][:8]}](https://www.youtube.com/playlist?list={js['items'][0]['id']['playlistId']})"
        		elif js['items'][0]['snippet']['description'] == '':
          			description = f"[None - {js['items'][0]['snippet']['publishedAt'][:9]}](https://www.youtube.com/watch?list={js['items'][0]['id']['playlistId']})"

      			if js['items'][1]['id']['kind'] == 'youtube#channel':
        			title1 = js['items'][1]['snippet']['title'][:10] + ' - Channel'
        			if len(js['items'][1]['snippet']['description']) > 29:
          				description1 = f"[{js['items'][1]['snippet']['description'][:20] + '...' + js['items'][1]['snippet']['publishedAt'][:8]}](https://www.youtube.com/channel/{js['items'][1]['snippet']['channelId']})"
        			elif len(js['items'][1]['snippet']['description']) <= 29:
          				description1					 = f"[{js['items'][1]['snippet']['description'][:20] + ' - ' + js['items'][1]['snippet']['publishedAt'][:8]}](https://www.youtube.com/channel/{js['items'][1]['id']['channelId']})"
        			elif js['items'][1]['snippet']['description'] == '':
          				description1 = f"[None](https://www.youtube.com/c/{js['items'][1]['snippet']['channelId']})"
      			elif js['items'][1]['id']['kind'] == 'youtube#video':
        			title1 = js['items'][1]['snippet']['title'][:8] + ' - Video'
        			if len(js['items'][1]['snippet']['description']) > 29:
          				description1 = f"[{js['items'][1]['snippet']['description'][:20] + '...' + js['items'][1]['snippet']['publishedAt'][:8]}](https://www.youtube.com/watch?v={js['items'][1]['id']['videoId']})"
        			elif len(js['items'][1]['snippet']['description']) <= 29:
          				description1 = f"[{js['items'][1]['snippet']['description'][:20] + ' - ' + js['items'][1]['snippet']['publishedAt'][:8]}](https://www.youtube.com/watch?list={js['items'][1]['id']['channelId']})"
        			elif js['items'][1]['snippet']['description'] == '':
          				description1 = f"[None](https://www.youtube.com/watch?v={js['items'][1]['id']['videoId']})"
      			elif js['items'][1]['id']['kind'] == 'youtube#playlist':
        			title1 = js['items'][1]['snippet']['title'][:11] + ' - Playlist'
        			if len(js['items'][1]['snippet']['description']) > 29:
          				description1 = f"[{js['items'][1]['snippet']['description'][:20] + '...' + js['items'][1]['snippet']['publishedAt'][:8]}](https://www.youtube.com/watch?v={js['items'][1]['id']['videoId']})"
        			elif len(js['items'][1]['snippet']['description']) <= 29:
          				description1 = f"[{js['items'][1]['snippet']['description'][:20] + ' - ' + js['items'][1]['snippet']['publishedAt'][:8]}](https://www.youtube.com/watch?list={js['items'][1]['id']['playlistId']})"
					elif js['items'][1]['snippet']['description'] == '':
          				description1 = f"[None - {js['items'][1]['snippet']['publishedAt'][:9]}](https://www.youtube.com/watch?list={js['items'][1]['id']['playlistId']})"
      
      				if js['items'][2]['id']['kind'] == 'youtube#channel':
        				title2 = js['items'][2]['snippet']['title'][:10] + ' - Channel'
        				if len(js['items'][2]['snippet']['description']) > 29:
          					description2 = f"[{js['items'][2]['snippet']['description'][:20] + '...' + js['items'][2]['snippet']['publishedAt'][:8]}](https://www.youtube.com/channel/{js['items'][2]['id']['channelId']})"
        				elif len(js['items'][2]['snippet']['description']) <= 29:
          					description2 = f"[{js['items'][2]['snippet']['description'][:20] + ' - ' + js['items'][2]['snippet']['publishedAt'][:8]}](https://www.youtube.com/channel/{js['items'][2]['id']['channelId']})"
        				elif len(js['items'][2]['snippet']['description']) >= 29:
          					description2 = f"[{js['items'][2]['snippet']['description'][:20] + ' - ' + js['items'][2]['snippet']['publishedAt'][:8]}](https://www.youtube.com/watch?list={js['items'][2]['id']['channelId']})"
        				elif js['items'][2]['snippet']['description'] == '':
          					description2 = f"[None](https://www.youtube.com/c/{js['items'][2]['snippet']['channelId']})"
      				elif js['items'][2]['id']['kind'] == 'youtube#video':
        				title2 = js['items'][2]['snippet']['title'][:8] + ' - Video'
        				if len(js['items'][2]['snippet']['description']) > 29:
          					description2 = f"[{js['items'][2]['snippet']['description'][:20] + '...' + js['items'][2]['snippet']['publishedAt'][:8]}](https://www.youtube.com/watch?v={js['items'][2]['id']['videoId']})"
        				elif len(js['items'][2]['snippet']['description']) <= 29:
          					description2 = f"[{js['items'][2]['snippet']['description'][:20] + ' - ' + js['items'][2]['snippet']['publishedAt'][:8]}](https://www.youtube.com/watch?v={js['items'][2]['id']['videoId']})"
        				elif js['items'][2]['snippet']['description'] == '':
          					description2 = f"[None](https://www.youtube.com/watch?v={js['items'][2]['id']['videoId']})"
      				elif js['items'][2]['id']['kind'] == 'youtube#playlist':
        				title2 = js['items'][2]['snippet']['title'][:11] + ' - Playlist'
        				if len(js['items'][2]['snippet']['description']) > 29:
          					description2 = f"[{js['items'][2]['snippet']['description'][:20] + '...' + js['items'][2]['snippet']['publishedAt'][:8]}](https://www.youtube.com/playlist?list={js['items'][2]['id']['playlistId']})"
        				elif len(js['items'][2]['snippet']['description']) >= 29:
          					description2 = f"[{js['items'][2]['snippet']['description'][:20] + ' - ' + js['items'][2]['snippet']['publishedAt'][:8]}](https://www.youtube.com/playlist?list={js['items'][2]['id']['playlistId']})"
        				elif js['items'][2]['snippet']['description'] == '':
          					description2 = f"[None - {js['items'][2]['snippet']['publishedAt'][:9]}](https://www.youtube.com/playlist?list={js['items'][2]['id']['playlistId']})"
      
      					if js['items'][3]['id']['kind'] == 'youtube#channel':
        					title3 = js['items'][3]['snippet']['title'][:10] + ' - Channel'
        					if len(js['items'][3]['snippet']['description']) > 29:
          						description3 = f"[{js['items'][3]['snippet']['description'][:20] + '...' + js['items'][3]['snippet']['publishedAt'][:8]}](https://www.youtube.com/channel/{js['items'][3]['snippet']['channelId']})"
        					elif len(js['items'][3]['snippet']['description']) <= 29:
          						description3 = f"[{js['items'][3]['snippet']['description'][:20] + ' - ' + js['items'][3]['snippet']['publishedAt'][:8]}](https://www.youtube.com/channel/{js['items'][3]['id']['channelId']})"
        					elif js['items'][3]['snippet']['description'] == '':
          						description3 = f"[None](https://www.youtube.com/channel/{js['items'][3]['snippet']['channelId']})"
      					elif js['items'][3]['id']['kind'] == 'youtube#video':
        					title3 = js['items'][3]['snippet']['title'][:8] + ' - Video'
        					if len(js['items'][3]['snippet']['description']) > 29:
          						description3 = f"[{js['items'][3]['snippet']['description'][:20] + '...' + js['items'][3]['snippet']['publishedAt'][:8]}](https://www.youtube.com/watch?v={js['items'][3]['id']['videoId']})"
        					elif len(js['items'][3]['snippet']['description']) <= 29:
          						description3 = f"[{js['items'][3]['snippet']['description'][:20] + ' - ' + js['items'][3]['snippet']['publishedAt'][:8]}](https://www.youtube.com/watch?v={js['items'][3]['id']['videoId']})"
        					elif js['items'][3]['snippet']['description'] == '':
          						description3 = f"[None](https://www.youtube.com/watch?v={js['items'][3]['id']['videoId']})"
      					elif js['items'][3]['id']['kind'] == 'youtube#playlist':
        					title3 = js['items'][3]['snippet']['title'][:11] + ' - Playlist'
        					if len(js['items'][3]['snippet']['description']) > 29:
          						description3 = f"[{js['items'][3]['snippet']['description'][:20] + '...' + js['items'][3]['snippet']['publishedAt'][:8]}](https://www.youtube.com/watch?v={js['items'][3]['id']['videoId']})"
        					elif len(js['items'][3]['snippet']['description']) <= 29:
          						description3 = f"[{js['items'][3]['snippet']['description'][:20] + ' - ' + js['items'][3]['snippet']['publishedAt'][:8]}](https://www.youtube.com/playlist?list={js['items'][3]['id']['playlistId']})"
        					elif js['items'][3]['snippet']['description'] == '':
          						description3 = f"[None - {js['items'][3]['snippet']['publishedAt'][:8]}](https://www.youtube.com/watch?list={js['items'][3]['id']['playlistId']}))"
      
      						if js['items'][4]['id']['kind'] == 'youtube#channel':
        						title4 = js['items'][4]['snippet']['title'][:10] + ' - Channel'
        						if len(js['items'][4]['snippet']['description']) > 29:
          							description4 = f"[{js['items'][4]['snippet']['description'][:20] + '...' + js['items'][4]['snippet']['publishedAt'][:8]}](https://www.youtube.com/channel/{js['items'][4]['snippet']['channelId']})"
        						elif len(js['items'][4]['snippet']['description']) <= 29:
          							description4 = f"[{js['items'][4]['snippet']['description'][:20] + ' - ' + js['items'][4]['snippet']['publishedAt'][:8]}](https://www.youtube.com/channel/{js['items'][4]['id']['channelId']})"
        						elif js['items'][4]['snippet']['description'] == '':
          							description4 = f"[None](https://www.youtube.com/channel/{js['items'][4]['snippet']['channelId']})"
      						elif js['items'][4]['id']['kind'] == 'youtube#video':
        						title4 = js['items'][4]['snippet']['title'][:8] + ' - Video'
        						if len(js['items'][4]['snippet']['description']) > 29:
          							description4 = f"[{js['items'][4]['snippet']['description'][:20] + '...' + js['items'][4]['snippet']['publishedAt'][:8]}](https://www.youtube.com/watch?v={js['items'][4]['id']['videoId']})"
        						elif len(js['items'][4]['snippet']['description']) <= 29:
          							description4 = f"[{js['items'][4]['snippet']['description'][:20] + ' - ' + js['items'][4]['snippet']['publishedAt'][:8]}](https://www.youtube.com/watch?v={js['items'][4]['id']['videoId']})"
        						elif js['items'][4]['snippet']['description'] == '':
          							description4 = f"[None](https://www.youtube.com/watch?v={js['items'][4]['id']['videoId']})"
      						elif js['items'][4]['id']['kind'] == 'youtube#playlist':
        						title4 = js['items'][4]['snippet']['title'][:11] + ' - Playlist'
        						if len(js['items'][4]['snippet']['description']) > 29:
          							description4 = f"[{js['items'][4]['snippet']['description'][:20] + '...' + js['items'][4]['snippet']['publishedAt'][:8]}](https://www.youtube.com/watch?v={js['items'][4]['id']['videoId']})"
        						elif len(js['items'][4]['snippet']['description']) >= 29:
          							description4 = f"[{js['items'][4]['snippet']['description'][:20] + ' - ' + js['items'][4]['snippet']['publishedAt'][:8]}](https://www.youtube.com/playlist?list={js['items'][4]['id']['channelId']})"
        						elif js['items'][4]['snippet']['description'] == '':
          							description4 = f"[None - {js['items'][4]['snippet']['publishedAt'][:8]}](https://www.youtube.com/watch?list={js['items'][4]['id']['playlistId']})"

      						youtube.add_field(
        						name=title,
        						value=description,
        						inline=False
      						)
      						youtube.add_field(
        						name=title1,
        						value=description1,
        						inline=False
      						)
      						youtube.add_field(
        						name=title2,
        						value=description2,
        						inline=False
      						)
      						youtube.add_field(
        						name=title3,
        						value=description3,
        						inline=False
      						)
      						youtube.add_field(
        						name=title4,
        						value=description4,
        						inline=False
      						)
      						youtube.set_thumbnail(url="https://play-lh.googleusercontent.com/lMoItBgdPPVDJsNOVtP26EKHePkwBg-PkuY9NOrc-fumRtTFP4XhpUNk_22syN4Datc")
      						await ctx.send(embed=youtube)
