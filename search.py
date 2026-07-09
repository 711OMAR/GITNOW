{
  "meta": {
    "title": "Atelier Codex — OSINT Source Library",
    "source": "Curated from Cyberflow's Academy OSINT compilation and a supplemental live-tooling list",
    "notice": "For lawful OSINT only: public data collection, no unauthorized access.",
    "categories": 49,
    "tools": 482,
    "integrable": 113,
    "keyless": 33,
    "linked": 45
  },
  "categories": {
    "General Search": [
      {
        "name": "Google"
      },
      {
        "name": "Bing"
      },
      {
        "name": "DuckDuckGo",
        "description": "Privacy-focused engine"
      },
      {
        "name": "Brave Search",
        "description": "Independent index"
      },
      {
        "name": "Mojeek",
        "description": "Independent, no tracking"
      },
      {
        "name": "Yandex",
        "description": "Strong for reverse-image & non-Latin"
      },
      {
        "name": "Wolfram Alpha",
        "description": "Computational answers"
      },
      {
        "name": "You.com",
        "description": "AI search"
      },
      {
        "name": "Lycos"
      },
      {
        "name": "Ask"
      },
      {
        "name": "Aol"
      },
      {
        "name": "Impersonal.me"
      }
    ],
    "National Search Engines": [
      {
        "name": "Baidu (China)"
      },
      {
        "name": "Naver (South Korea)"
      },
      {
        "name": "Goo (Japan)"
      },
      {
        "name": "Seznam (Czechia)"
      },
      {
        "name": "Onet.pl (Poland)"
      },
      {
        "name": "Walla (Israel)"
      },
      {
        "name": "SAPO (Portugal)"
      },
      {
        "name": "Parseek (Iran)"
      },
      {
        "name": "Alleba (Philippines)"
      },
      {
        "name": "Eniro (Sweden)"
      },
      {
        "name": "Search.ch (Switzerland)"
      },
      {
        "name": "Najdi.si (Slovenia)"
      }
    ],
    "Meta & Clustering Search": [
      {
        "name": "Carrot2",
        "description": "Clusters results into topics"
      },
      {
        "name": "etools"
      },
      {
        "name": "AllTheInternet"
      },
      {
        "name": "Qwant",
        "description": "EU engine over Bing"
      },
      {
        "name": "Swisscows"
      },
      {
        "name": "Goofram"
      },
      {
        "name": "iZito"
      },
      {
        "name": "Zapmeta"
      }
    ],
    "Specialty Search": [
      {
        "name": "Shodan",
        "description": "IoT/host search engine",
        "integrable": true,
        "entity_types": [
          "ip",
          "domain"
        ],
        "keyless": false
      },
      {
        "name": "Netlas.io",
        "description": "Host & certificate search",
        "integrable": true,
        "entity_types": [
          "ip",
          "domain"
        ],
        "keyless": false
      },
      {
        "name": "Criminal IP",
        "description": "Attack-surface & CTI search",
        "integrable": true,
        "entity_types": [
          "ip",
          "domain"
        ],
        "keyless": false
      },
      {
        "name": "Intelligence X",
        "description": "Search leaks, darknet, pastes",
        "integrable": true,
        "entity_types": [
          "email",
          "domain"
        ],
        "keyless": false
      },
      {
        "name": "Internet Archive",
        "description": "Historical web & media"
      },
      {
        "name": "OCCRP Aleph",
        "description": "Investigative journalism datasets"
      },
      {
        "name": "GrayhatWarfare",
        "description": "Open S3 bucket search",
        "url": "https://grayhatwarfare.com/"
      },
      {
        "name": "BeVigil",
        "description": "Assets from mobile apps",
        "integrable": true,
        "entity_types": [
          "domain"
        ],
        "keyless": false
      },
      {
        "name": "Million Short"
      },
      {
        "name": "WIPO",
        "description": "Patents"
      },
      {
        "name": "WorldWideScience.org"
      },
      {
        "name": "Mamont"
      },
      {
        "name": "LeakIX",
        "description": "Search engine for exposed services, databases & internet-facing assets",
        "url": "https://leakix.net/",
        "integrable": true,
        "entity_types": [
          "domain",
          "ip"
        ],
        "keyless": false
      }
    ],
    "Similar Sites": [
      {
        "name": "SimilarSites"
      },
      {
        "name": "SitesLike"
      },
      {
        "name": "Google Similar Pages"
      }
    ],
    "Documents & Slides": [
      {
        "name": "Scribd"
      },
      {
        "name": "SlideShare"
      },
      {
        "name": "Offshore Leaks Database",
        "description": "ICIJ leaked corporate records"
      },
      {
        "name": "Free Full PDF"
      },
      {
        "name": "Find-pdf-doc"
      },
      {
        "name": "de digger",
        "description": "Public Google Drive files"
      }
    ],
    "File Search": [
      {
        "name": "FilePursuit"
      },
      {
        "name": "NAPALM FTP Indexer"
      },
      {
        "name": "File Search Engine"
      },
      {
        "name": "SearchFiles.de"
      },
      {
        "name": "FileListing"
      }
    ],
    "Pastebins": [
      {
        "name": "Pastebin"
      },
      {
        "name": "GitHub Gist"
      },
      {
        "name": "0bin"
      },
      {
        "name": "hastebin"
      },
      {
        "name": "controlc"
      },
      {
        "name": "Rentry"
      },
      {
        "name": "Katbin"
      },
      {
        "name": "dpaste"
      },
      {
        "name": "ivpaste"
      },
      {
        "name": "justpaste"
      },
      {
        "name": "doxbin",
        "description": "Hacker-run paste site"
      }
    ],
    "Code Search": [
      {
        "name": "GitHub",
        "description": "Code, users, repos, gists",
        "integrable": true,
        "entity_types": [
          "username",
          "email",
          "code"
        ],
        "keyless": false
      },
      {
        "name": "grep.app",
        "description": "Regex across public GitHub"
      },
      {
        "name": "SourceGraph",
        "description": "Search millions of repos"
      },
      {
        "name": "PublicWWW",
        "description": "Search site source markup"
      },
      {
        "name": "NerdyData",
        "description": "Source-code search engine"
      },
      {
        "name": "SearchCode"
      },
      {
        "name": "Code Finder"
      },
      {
        "name": "AnalyzeID",
        "description": "Other sites owned by same person"
      },
      {
        "name": "Sourcebot",
        "description": "Self-hosted repo index/search"
      }
    ],
    "Social Networks": [
      {
        "name": "Facebook"
      },
      {
        "name": "Instagram"
      },
      {
        "name": "LinkedIn"
      },
      {
        "name": "Twitter/X"
      },
      {
        "name": "Reddit"
      },
      {
        "name": "VKontakte"
      },
      {
        "name": "Weibo (China)"
      },
      {
        "name": "Odnoklassniki (Russia)"
      },
      {
        "name": "Tumblr"
      },
      {
        "name": "Pinterest"
      },
      {
        "name": "Tinder"
      },
      {
        "name": "Xing"
      },
      {
        "name": "Mixi (Japan)"
      },
      {
        "name": "Qzone (China)"
      }
    ],
    "Twitter/X Tools": [
      {
        "name": "Twitter Advanced Search"
      },
      {
        "name": "TweetDeck"
      },
      {
        "name": "Audiense",
        "description": "Audience analytics"
      },
      {
        "name": "Brandwatch"
      },
      {
        "name": "Buzzsumo"
      },
      {
        "name": "Social Searcher",
        "url": "https://www.social-searcher.com/"
      },
      {
        "name": "Foller.me",
        "description": "Account analytics"
      },
      {
        "name": "OneMillionTweetMap"
      },
      {
        "name": "Trends24"
      },
      {
        "name": "Twitter Audit"
      },
      {
        "name": "Sentiment140"
      },
      {
        "name": "Castrick",
        "description": "Find accounts by email/username/phone",
        "integrable": true,
        "entity_types": [
          "email",
          "username",
          "phone"
        ],
        "keyless": false
      },
      {
        "name": "Epieos",
        "description": "Accounts via email & phone",
        "integrable": true,
        "entity_types": [
          "email",
          "phone"
        ],
        "keyless": false
      },
      {
        "name": "Predicta Search",
        "description": "Accounts via email & phone",
        "integrable": true,
        "entity_types": [
          "email",
          "phone"
        ],
        "keyless": false
      },
      {
        "name": "ExportData",
        "description": "Historical tweets/followers export"
      }
    ],
    "Facebook Tools": [
      {
        "name": "Facebook Search"
      },
      {
        "name": "Lookup-ID.com",
        "description": "Find profile/group/page ID"
      },
      {
        "name": "Find my Facebook ID"
      },
      {
        "name": "haveibeenzuckered",
        "description": "Check 2019 breach by phone",
        "integrable": true,
        "entity_types": [
          "phone"
        ],
        "keyless": false
      },
      {
        "name": "SearchIsBack"
      },
      {
        "name": "Facebook Friend List Scraper"
      },
      {
        "name": "Wolfram Alpha Facebook Report"
      }
    ],
    "Instagram Tools": [
      {
        "name": "Osintgram",
        "description": "Interactive IG account analysis",
        "integrable": true,
        "entity_types": [
          "username"
        ],
        "keyless": false
      },
      {
        "name": "Toutatis",
        "description": "Extract emails/phone from IG",
        "integrable": true,
        "entity_types": [
          "username"
        ],
        "keyless": false
      },
      {
        "name": "Sterra",
        "description": "Export & analyse followers",
        "integrable": true,
        "entity_types": [
          "username"
        ],
        "keyless": false
      },
      {
        "name": "Picodash"
      },
      {
        "name": "Iconosquare"
      },
      {
        "name": "Pictriev"
      }
    ],
    "Reddit Tools": [
      {
        "name": "Pushshift API",
        "description": "Historical Reddit data",
        "integrable": true,
        "entity_types": [
          "username"
        ],
        "keyless": false
      },
      {
        "name": "Pullpush",
        "description": "Deleted/removed posts & comments",
        "integrable": true,
        "entity_types": [
          "username"
        ],
        "keyless": false
      },
      {
        "name": "Arctic Shift",
        "description": "Access large Reddit dumps",
        "integrable": true,
        "entity_types": [
          "username"
        ],
        "keyless": false
      },
      {
        "name": "Reddit User Analyser"
      },
      {
        "name": "RedditMetis",
        "description": "User summary & stats"
      },
      {
        "name": "Reddit Comment Search"
      },
      {
        "name": "REDARCS",
        "description": "Reddit archives 2005-2023"
      },
      {
        "name": "Universal Scammer List"
      },
      {
        "name": "Subreddits",
        "description": "Discover subreddits"
      }
    ],
    "VKontakte Tools": [
      {
        "name": "VK5"
      },
      {
        "name": "VK People Search"
      },
      {
        "name": "VK.watch"
      },
      {
        "name": "VK Community Search"
      },
      {
        "name": "Barkov.net"
      },
      {
        "name": "VK Parser"
      },
      {
        "name": "Report Tree"
      }
    ],
    "Telegram Tools": [
      {
        "name": "Telegago",
        "description": "Google search for public channels"
      },
      {
        "name": "Telegram Nearby Map",
        "description": "Locate nearby users"
      },
      {
        "name": "Maltego Telegram",
        "description": "Maltego transforms for Telegram"
      }
    ],
    "LinkedIn Tools": [
      {
        "name": "LinkedIn"
      },
      {
        "name": "RecruitEm",
        "description": "X-ray search LinkedIn"
      },
      {
        "name": "FTL",
        "description": "Find profile emails"
      }
    ],
    "Username Check": [
      {
        "name": "Sherlock",
        "description": "Username across many sites",
        "integrable": true,
        "entity_types": [
          "username"
        ],
        "keyless": true
      },
      {
        "name": "Maigret",
        "description": "Dossier by username",
        "integrable": true,
        "entity_types": [
          "username"
        ],
        "keyless": true,
        "url": "https://github.com/soxoj/maigret"
      },
      {
        "name": "Blackbird",
        "description": "Username across 600+ sites",
        "integrable": true,
        "entity_types": [
          "username"
        ],
        "keyless": true,
        "url": "https://github.com/p1ngul1n0/blackbird"
      },
      {
        "name": "WhatsMyName",
        "description": "Username enumeration",
        "integrable": true,
        "entity_types": [
          "username"
        ],
        "keyless": true,
        "url": "https://whatsmyname.app/"
      },
      {
        "name": "NexFil",
        "description": "Username across social sites",
        "integrable": true,
        "entity_types": [
          "username"
        ],
        "keyless": true
      },
      {
        "name": "Snoop",
        "description": "Nickname search",
        "integrable": true,
        "entity_types": [
          "username"
        ],
        "keyless": false
      },
      {
        "name": "IDCrawl",
        "description": "Name/username in social networks",
        "integrable": true,
        "entity_types": [
          "username"
        ],
        "keyless": false
      },
      {
        "name": "Namechk"
      },
      {
        "name": "NameCheckr"
      },
      {
        "name": "Name Checkup"
      },
      {
        "name": "CheckUser"
      },
      {
        "name": "Digital Footprint Check"
      },
      {
        "name": "User Search",
        "description": "Across 3000+ sites"
      },
      {
        "name": "User Searcher",
        "description": "Username in 2000+ sites"
      },
      {
        "name": "Seekr"
      },
      {
        "name": "SherlockEye"
      },
      {
        "name": "Tookie OSINT",
        "description": "Username & account OSINT automation toolkit",
        "url": "https://github.com/Alfredredbird/tookie-osint",
        "integrable": true,
        "entity_types": [
          "username"
        ],
        "keyless": true
      },
      {
        "name": "SocialEye",
        "description": "Social-intelligence search platform",
        "url": "https://socialeye.net/",
        "integrable": true,
        "entity_types": [
          "username"
        ],
        "keyless": false
      },
      {
        "name": "Lookups.io",
        "description": "Public lookup & identity search tools",
        "url": "https://lookups.io/",
        "integrable": true,
        "entity_types": [
          "username",
          "email",
          "phone"
        ],
        "keyless": false
      },
      {
        "name": "Intelbase",
        "description": "Intelligence research platform",
        "url": "https://intelbase.is/"
      },
      {
        "name": "Robin",
        "description": "AI-assisted OSINT investigation tool",
        "url": "https://github.com/apurvsinghgautam/robin",
        "integrable": true,
        "entity_types": [
          "username"
        ],
        "keyless": true
      },
      {
        "name": "IntelTrace",
        "description": "OSINT investigation toolkit",
        "url": "https://github.com/Gowtham-Darkseid/IntelTrace",
        "integrable": true,
        "entity_types": [
          "username"
        ],
        "keyless": true
      },
      {
        "name": "The OSINT Vault — Username Guide",
        "description": "Username OSINT techniques & resources",
        "url": "https://theosintvault.io/username-osint-guide"
      }
    ],
    "People Investigations": [
      {
        "name": "BeenVerified"
      },
      {
        "name": "Spokeo"
      },
      {
        "name": "ThatsThem",
        "description": "Reverse email/phone/address",
        "integrable": true,
        "entity_types": [
          "email",
          "phone"
        ],
        "keyless": false,
        "url": "https://thatsthem.com/"
      },
      {
        "name": "FaceCheck.ID",
        "description": "Search internet by face",
        "integrable": true,
        "entity_types": [
          "image"
        ],
        "keyless": false,
        "url": "https://facecheck.id/"
      },
      {
        "name": "FamilyTreeNow"
      },
      {
        "name": "FamilySearch"
      },
      {
        "name": "Ancestry"
      },
      {
        "name": "Judyrecords",
        "description": "US court cases"
      },
      {
        "name": "UniCourt",
        "description": "US court cases"
      },
      {
        "name": "OpenSanctions",
        "description": "Sanctions & PEPs",
        "integrable": true,
        "entity_types": [
          "person",
          "company"
        ],
        "keyless": false
      },
      {
        "name": "Voter Records",
        "description": "US voter records"
      },
      {
        "name": "Whitepages"
      },
      {
        "name": "Homemetry",
        "description": "Reverse address"
      },
      {
        "name": "BOP Inmate Locator (US)"
      },
      {
        "name": "VineLink"
      },
      {
        "name": "Black Book Online"
      },
      {
        "name": "Canada411"
      }
    ],
    "Email Search": [
      {
        "name": "Have I Been Pwned",
        "description": "Breach check by email",
        "integrable": true,
        "entity_types": [
          "email"
        ],
        "keyless": false
      },
      {
        "name": "Hunter",
        "description": "Find & verify company emails",
        "integrable": true,
        "entity_types": [
          "email",
          "domain"
        ],
        "keyless": false
      },
      {
        "name": "DeHashed",
        "description": "Breach/credential search",
        "integrable": true,
        "entity_types": [
          "email",
          "username"
        ],
        "keyless": false
      },
      {
        "name": "LeakCheck",
        "description": "Breach search engine",
        "integrable": true,
        "entity_types": [
          "email",
          "username"
        ],
        "keyless": false
      },
      {
        "name": "LeakRadar",
        "description": "Stealer-log monitoring",
        "integrable": true,
        "entity_types": [
          "email",
          "domain"
        ],
        "keyless": false
      },
      {
        "name": "Holehe",
        "description": "Which sites an email is registered on",
        "integrable": true,
        "entity_types": [
          "email"
        ],
        "keyless": true
      },
      {
        "name": "GHunt",
        "description": "Investigate Google accounts",
        "integrable": true,
        "entity_types": [
          "email"
        ],
        "keyless": false
      },
      {
        "name": "h8mail",
        "description": "Breach hunting & email OSINT",
        "integrable": true,
        "entity_types": [
          "email"
        ],
        "keyless": false
      },
      {
        "name": "Gitrecon",
        "description": "Emails/names from GitHub",
        "integrable": true,
        "entity_types": [
          "username",
          "email"
        ],
        "keyless": false
      },
      {
        "name": "EmailHippo",
        "description": "Verify address existence",
        "integrable": true,
        "entity_types": [
          "email"
        ],
        "keyless": false
      },
      {
        "name": "Email Format",
        "description": "Company email patterns",
        "integrable": true,
        "entity_types": [
          "domain"
        ],
        "keyless": false
      },
      {
        "name": "Email Permutator",
        "description": "Generate candidate addresses",
        "integrable": true,
        "entity_types": [
          "email"
        ],
        "keyless": false
      },
      {
        "name": "Snov.io",
        "description": "Find emails on any site",
        "integrable": true,
        "entity_types": [
          "domain"
        ],
        "keyless": false
      },
      {
        "name": "Reacher",
        "description": "Open-source verification API",
        "integrable": true,
        "entity_types": [
          "email"
        ],
        "keyless": true
      },
      {
        "name": "SherlockEye"
      },
      {
        "name": "Pipl"
      },
      {
        "name": "Peepmail"
      },
      {
        "name": "VoilaNorbert"
      },
      {
        "name": "Toofr"
      },
      {
        "name": "Verify Email"
      },
      {
        "name": "HackCheck",
        "description": "Breach & exposure lookup service",
        "url": "https://hackcheck.io/",
        "integrable": true,
        "entity_types": [
          "email",
          "domain"
        ],
        "keyless": false
      }
    ],
    "Phone Research": [
      {
        "name": "PhoneInfoga",
        "description": "Phone number recon framework",
        "integrable": true,
        "entity_types": [
          "phone"
        ],
        "keyless": true
      },
      {
        "name": "Twilio Lookup",
        "description": "Carrier/line-type via API",
        "integrable": true,
        "entity_types": [
          "phone"
        ],
        "keyless": false
      },
      {
        "name": "Truecaller",
        "description": "Global reverse phone"
      },
      {
        "name": "FreeCarrierLookup",
        "description": "Carrier & line type",
        "integrable": true,
        "entity_types": [
          "phone"
        ],
        "keyless": false
      },
      {
        "name": "CallerID Test"
      },
      {
        "name": "Phone Validator"
      },
      {
        "name": "Sync.ME"
      },
      {
        "name": "Spy Dialer"
      },
      {
        "name": "EmobileTracker"
      },
      {
        "name": "USPhoneBook"
      },
      {
        "name": "Reverse Phone Lookup"
      },
      {
        "name": "Infobel"
      }
    ],
    "Vehicle Research": [
      {
        "name": "FaxVIN",
        "description": "Plate → VIN & history"
      },
      {
        "name": "EpicVIN",
        "description": "VIN reports & plate lookup"
      }
    ],
    "Company Research": [
      {
        "name": "OpenCorporates",
        "description": "Global company registry",
        "integrable": true,
        "entity_types": [
          "company"
        ],
        "keyless": false
      },
      {
        "name": "EDGAR (SEC)",
        "description": "US public-company filings",
        "integrable": true,
        "entity_types": [
          "company"
        ],
        "keyless": false
      },
      {
        "name": "Crunchbase",
        "description": "Startup/funding data",
        "integrable": true,
        "entity_types": [
          "company"
        ],
        "keyless": false
      },
      {
        "name": "Bloomberg"
      },
      {
        "name": "Better Business Bureau"
      },
      {
        "name": "OpenOwnership",
        "description": "Beneficial ownership"
      },
      {
        "name": "Corporate Information"
      },
      {
        "name": "CorporationWiki"
      },
      {
        "name": "Bureau van Dijk"
      },
      {
        "name": "Glassdoor"
      },
      {
        "name": "Hoovers"
      },
      {
        "name": "YouControl"
      },
      {
        "name": "Forbes Global 2000"
      },
      {
        "name": "European Business Register"
      },
      {
        "name": "Europages"
      }
    ],
    "Domain & IP Research": [
      {
        "name": "crt.sh",
        "description": "Certificate transparency logs",
        "integrable": true,
        "entity_types": [
          "domain"
        ],
        "keyless": true
      },
      {
        "name": "VirusTotal",
        "description": "Domains/IPs/URLs/files reputation",
        "integrable": true,
        "entity_types": [
          "domain",
          "ip",
          "url",
          "hash"
        ],
        "keyless": false
      },
      {
        "name": "SecurityTrails",
        "description": "Current & historical DNS/WHOIS",
        "integrable": true,
        "entity_types": [
          "domain",
          "ip"
        ],
        "keyless": false
      },
      {
        "name": "urlscan.io",
        "description": "Scan & analyse websites",
        "integrable": true,
        "entity_types": [
          "url",
          "domain"
        ],
        "keyless": false
      },
      {
        "name": "BuiltWith",
        "description": "Technology profiling",
        "integrable": true,
        "entity_types": [
          "domain"
        ],
        "keyless": false
      },
      {
        "name": "DNSDumpster",
        "description": "Discover hosts for a domain",
        "integrable": true,
        "entity_types": [
          "domain"
        ],
        "keyless": true
      },
      {
        "name": "ViewDNS.info",
        "description": "DNS/WHOIS toolset",
        "integrable": true,
        "entity_types": [
          "domain",
          "ip"
        ],
        "keyless": false
      },
      {
        "name": "Robtex",
        "description": "Reverse DNS/WHOIS research",
        "integrable": true,
        "entity_types": [
          "domain",
          "ip"
        ],
        "keyless": false
      },
      {
        "name": "Validin",
        "description": "Free current/historical DNS",
        "integrable": true,
        "entity_types": [
          "domain"
        ],
        "keyless": false
      },
      {
        "name": "Pulsedive",
        "description": "Community threat intel",
        "integrable": true,
        "entity_types": [
          "domain",
          "ip",
          "url"
        ],
        "keyless": false
      },
      {
        "name": "URLVoid",
        "description": "Domain reputation blacklists",
        "integrable": true,
        "entity_types": [
          "domain"
        ],
        "keyless": false
      },
      {
        "name": "Web-Check",
        "description": "Site & server metadata",
        "integrable": true,
        "entity_types": [
          "domain"
        ],
        "keyless": true,
        "url": "https://github.com/Lissy93/web-check"
      },
      {
        "name": "Webscout",
        "description": "Scaled IP/domain intel",
        "integrable": true,
        "entity_types": [
          "ip",
          "domain"
        ],
        "keyless": false
      },
      {
        "name": "Threat Jammer",
        "description": "Risk scoring from CTI",
        "integrable": true,
        "entity_types": [
          "ip"
        ],
        "keyless": false
      },
      {
        "name": "PhishStats",
        "description": "Phishing URL feed",
        "integrable": true,
        "entity_types": [
          "url",
          "domain"
        ],
        "keyless": false
      },
      {
        "name": "Hudson Rock",
        "description": "Infostealer exposure check",
        "integrable": true,
        "entity_types": [
          "domain",
          "email"
        ],
        "keyless": false
      },
      {
        "name": "Domain Dossier"
      },
      {
        "name": "Central Ops"
      },
      {
        "name": "Who.is",
        "description": "WHOIS lookup"
      },
      {
        "name": "Whoisology"
      },
      {
        "name": "DomainTools",
        "description": "WHOIS & historical"
      },
      {
        "name": "intoDNS"
      },
      {
        "name": "DNSViz"
      },
      {
        "name": "IPVoid",
        "description": "IP toolset"
      },
      {
        "name": "IP Location"
      },
      {
        "name": "IPFingerprints"
      },
      {
        "name": "MaxMind"
      },
      {
        "name": "Netcraft Site Report"
      },
      {
        "name": "SubDomainRadar.io",
        "description": "Subdomain finder",
        "integrable": true,
        "entity_types": [
          "domain"
        ],
        "keyless": false
      },
      {
        "name": "Squatm3gator",
        "description": "Cybersquat domain enum"
      },
      {
        "name": "ExoneraTor",
        "description": "Was IP a Tor relay?"
      },
      {
        "name": "WiGLE",
        "description": "Wardriving Wi-Fi database",
        "integrable": true,
        "entity_types": [
          "wifi"
        ],
        "keyless": false
      },
      {
        "name": "You Get Signal"
      },
      {
        "name": "Unfurl",
        "description": "Break a URL into its investigable parts",
        "url": "https://dfir.blog/unfurl/",
        "integrable": true,
        "entity_types": [
          "url"
        ],
        "keyless": true
      },
      {
        "name": "DorkSearch",
        "description": "Build Google-dork queries fast",
        "url": "https://dorksearch.com/"
      },
      {
        "name": "OathNet",
        "description": "Online intelligence research resource",
        "url": "https://oathnet.org/"
      }
    ],
    "Keyword Research": [
      {
        "name": "Google Trends"
      },
      {
        "name": "Google Ads Keyword Planner"
      },
      {
        "name": "Ubersuggest"
      },
      {
        "name": "KeywordTool"
      },
      {
        "name": "Yandex Wordstat"
      },
      {
        "name": "Soovle"
      },
      {
        "name": "Answer/One Look Reverse Dictionary"
      }
    ],
    "Web History & Capture": [
      {
        "name": "Wayback Machine",
        "description": "Historical snapshots",
        "integrable": true,
        "entity_types": [
          "domain",
          "url"
        ],
        "keyless": true
      },
      {
        "name": "Archive.is",
        "description": "On-demand page snapshots",
        "integrable": true,
        "entity_types": [
          "url"
        ],
        "keyless": true
      },
      {
        "name": "CachedView"
      },
      {
        "name": "stored.website"
      },
      {
        "name": "waybackpy",
        "description": "Wayback API CLI",
        "integrable": true,
        "entity_types": [
          "domain"
        ],
        "keyless": true
      }
    ],
    "Image Search & Analysis": [
      {
        "name": "Google Lens",
        "description": "Reverse image"
      },
      {
        "name": "Yandex Images",
        "description": "Strong reverse image"
      },
      {
        "name": "TinEye",
        "description": "Reverse image engine",
        "integrable": true,
        "entity_types": [
          "image"
        ],
        "keyless": false
      },
      {
        "name": "Bing Visual Search"
      },
      {
        "name": "PimEyes",
        "description": "Face search engine",
        "integrable": true,
        "entity_types": [
          "image"
        ],
        "keyless": false
      },
      {
        "name": "FaceCheck.ID",
        "description": "Facial recognition",
        "integrable": true,
        "entity_types": [
          "image"
        ],
        "keyless": false,
        "url": "https://facecheck.id/"
      },
      {
        "name": "Search4faces",
        "description": "Find people by photo",
        "integrable": true,
        "entity_types": [
          "image"
        ],
        "keyless": false
      },
      {
        "name": "PicTriev"
      },
      {
        "name": "ExifTool",
        "description": "Read file metadata",
        "integrable": true,
        "entity_types": [
          "image"
        ],
        "keyless": true
      },
      {
        "name": "ExifLooter",
        "description": "Extract EXIF geolocation",
        "integrable": true,
        "entity_types": [
          "image"
        ],
        "keyless": true
      },
      {
        "name": "Jimpl",
        "description": "Online EXIF viewer",
        "integrable": true,
        "entity_types": [
          "image"
        ],
        "keyless": false
      },
      {
        "name": "Jeffrey's EXIF Viewer"
      },
      {
        "name": "FotoForensics",
        "description": "Error-level analysis"
      },
      {
        "name": "Forensically"
      },
      {
        "name": "GeoSpy",
        "description": "AI image geolocation",
        "integrable": true,
        "entity_types": [
          "image"
        ],
        "keyless": false
      },
      {
        "name": "GeoSpyer"
      },
      {
        "name": "SmartImage",
        "description": "Reverse-image search aggregator utility",
        "url": "https://github.com/Decimation/SmartImage",
        "integrable": true,
        "entity_types": [
          "image"
        ],
        "keyless": true
      },
      {
        "name": "Image Matching WebUI",
        "description": "Image similarity & feature-matching interface",
        "url": "https://github.com/Vincentqyw/image-matching-webui",
        "integrable": true,
        "entity_types": [
          "image"
        ],
        "keyless": true
      },
      {
        "name": "ShadowFinder",
        "description": "Estimate location from shadow length & timestamp",
        "url": "https://github.com/bellingcat/ShadowFinder",
        "integrable": true,
        "entity_types": [
          "image"
        ],
        "keyless": true
      },
      {
        "name": "PANO",
        "description": "Panorama / image OSINT tooling",
        "url": "https://github.com/ALW1EZ/PANO",
        "integrable": true,
        "entity_types": [
          "image"
        ],
        "keyless": true
      },
      {
        "name": "GeoAxis AI",
        "description": "AI-assisted geolocation & image intelligence",
        "url": "https://geoaxis.ai/"
      },
      {
        "name": "Revealer",
        "description": "Image & intelligence analysis resource",
        "url": "https://revealer.us/"
      }
    ],
    "Video Tools": [
      {
        "name": "YouTube Data Viewer",
        "description": "Metadata & thumbnails",
        "integrable": true,
        "entity_types": [
          "url"
        ],
        "keyless": false
      },
      {
        "name": "YouTube Metadata"
      },
      {
        "name": "YouTube Geofind",
        "description": "Videos by location"
      },
      {
        "name": "Filmot",
        "description": "Search within YouTube subtitles"
      },
      {
        "name": "Find YouTube Video",
        "description": "Recover deleted videos"
      },
      {
        "name": "yt-dlp",
        "description": "Download video+metadata",
        "integrable": true,
        "entity_types": [
          "url"
        ],
        "keyless": true
      },
      {
        "name": "Insecam",
        "description": "Open camera directory",
        "url": "https://www.insecam.org/",
        "caution": "Indexes exposed cameras. Lawful research only — do not access private feeds."
      },
      {
        "name": "EarthCam",
        "description": "Live webcams"
      }
    ],
    "Academic & Grey Literature": [
      {
        "name": "Google Scholar"
      },
      {
        "name": "JSTOR"
      },
      {
        "name": "PubMed"
      },
      {
        "name": "ScienceDirect"
      },
      {
        "name": "ResearchGate"
      },
      {
        "name": "CORE"
      },
      {
        "name": "BASE"
      },
      {
        "name": "OA.mg",
        "description": "240M+ works"
      },
      {
        "name": "OpenGrey"
      },
      {
        "name": "Semantic Scholar"
      }
    ],
    "Geospatial & Mapping": [
      {
        "name": "Google Earth Pro"
      },
      {
        "name": "Google Maps"
      },
      {
        "name": "OpenStreetMap"
      },
      {
        "name": "Sentinel Hub",
        "description": "Satellite imagery"
      },
      {
        "name": "Maxar",
        "description": "High-res satellite"
      },
      {
        "name": "EarthExplorer (USGS)"
      },
      {
        "name": "SAS Planet",
        "description": "Download/stitch satellite tiles"
      },
      {
        "name": "Liveuamap",
        "description": "Live conflict map"
      },
      {
        "name": "Bellingcat WorldMap"
      },
      {
        "name": "Overpass/Wikimapia"
      },
      {
        "name": "SunCalc",
        "description": "Sun position by time"
      },
      {
        "name": "Instant Google Street View"
      },
      {
        "name": "Pic2Map"
      },
      {
        "name": "Windy",
        "description": "Weather map"
      },
      {
        "name": "Worldwide OSINT Tools Map"
      }
    ],
    "News": [
      {
        "name": "Google News"
      },
      {
        "name": "Bing News"
      },
      {
        "name": "Reuters"
      },
      {
        "name": "AP"
      },
      {
        "name": "AFP"
      },
      {
        "name": "Euronews"
      },
      {
        "name": "Factiva"
      },
      {
        "name": "Silobreaker"
      },
      {
        "name": "NewsLookup"
      },
      {
        "name": "Newspaper Map"
      },
      {
        "name": "Newseum Front Pages"
      },
      {
        "name": "1st Headlines"
      }
    ],
    "News Digest": [
      {
        "name": "Flipboard"
      },
      {
        "name": "News360"
      },
      {
        "name": "Inshorts"
      },
      {
        "name": "Storyful"
      },
      {
        "name": "Spike"
      },
      {
        "name": "Reeder"
      }
    ],
    "Fact Checking": [
      {
        "name": "Snopes"
      },
      {
        "name": "Full Fact"
      },
      {
        "name": "Emergent"
      },
      {
        "name": "CaptainFact"
      },
      {
        "name": "Verification Handbook"
      }
    ],
    "Data & Statistics": [
      {
        "name": "CIA World Factbook"
      },
      {
        "name": "World Bank Data"
      },
      {
        "name": "Eurostat"
      },
      {
        "name": "UN Data"
      },
      {
        "name": "OECD Data"
      },
      {
        "name": "Statista"
      },
      {
        "name": "Knoema"
      },
      {
        "name": "Trading Economics"
      },
      {
        "name": "Gapminder"
      },
      {
        "name": "Google Public Data Explorer"
      },
      {
        "name": "UN COMTRADE"
      },
      {
        "name": "Transparency.org CPI"
      },
      {
        "name": "Nation Master"
      },
      {
        "name": "data.gov.uk"
      }
    ],
    "Web Monitoring": [
      {
        "name": "Google Alerts",
        "description": "Change/notification service"
      },
      {
        "name": "visualping",
        "description": "Page-change monitoring"
      },
      {
        "name": "changedetection.io",
        "description": "Open-source monitor"
      },
      {
        "name": "Mention"
      },
      {
        "name": "Talkwalker"
      },
      {
        "name": "Feedly"
      },
      {
        "name": "RSS Bridge"
      },
      {
        "name": "FollowThatPage"
      },
      {
        "name": "Distill/versionista"
      },
      {
        "name": "OnWebChange"
      }
    ],
    "Browsers": [
      {
        "name": "Tor Browser",
        "description": "Anonymous browsing"
      },
      {
        "name": "Brave",
        "description": "Ad/tracker blocking"
      },
      {
        "name": "Firefox"
      },
      {
        "name": "Chrome"
      },
      {
        "name": "Yandex Browser"
      },
      {
        "name": "Vivaldi"
      },
      {
        "name": "Epic Privacy Browser"
      }
    ],
    "Offline Browsing": [
      {
        "name": "HTTrack",
        "description": "Mirror a site locally"
      },
      {
        "name": "Cyotek WebCopy"
      },
      {
        "name": "A1 Website Download"
      },
      {
        "name": "SiteSucker"
      },
      {
        "name": "Offliberty"
      },
      {
        "name": "Website Ripper Copier"
      }
    ],
    "VPN Resources": [
      {
        "name": "That One Privacy Guy VPN Comparison"
      },
      {
        "name": "TorrentFreak VPN List"
      },
      {
        "name": "OffShore.cat"
      }
    ],
    "Data Visualization": [
      {
        "name": "D3.js"
      },
      {
        "name": "Chart.js"
      },
      {
        "name": "Leaflet"
      },
      {
        "name": "Highcharts"
      },
      {
        "name": "Plotly"
      },
      {
        "name": "Datawrapper"
      },
      {
        "name": "Observable"
      },
      {
        "name": "Vis.js"
      },
      {
        "name": "Tableau Public"
      },
      {
        "name": "Flourish/Infogram"
      },
      {
        "name": "Cacoo"
      },
      {
        "name": "Lucidchart"
      }
    ],
    "Social Network Analysis": [
      {
        "name": "Gephi",
        "description": "Graph/network visualization"
      },
      {
        "name": "ORA"
      },
      {
        "name": "Sentinel Visualizer"
      },
      {
        "name": "Visual Investigative Scenarios"
      },
      {
        "name": "Wynyard Group"
      }
    ],
    "Privacy & Encryption": [
      {
        "name": "KeePass",
        "description": "Password manager"
      },
      {
        "name": "GnuPG",
        "description": "OpenPGP encryption"
      },
      {
        "name": "Proton Mail"
      },
      {
        "name": "Tails",
        "description": "Amnesic live OS"
      },
      {
        "name": "Qubes OS",
        "description": "Isolation-based OS"
      },
      {
        "name": "Signal-style: Wickr"
      },
      {
        "name": "uBlock Origin"
      },
      {
        "name": "Privacy Badger"
      },
      {
        "name": "NoScript"
      },
      {
        "name": "HTTPS Everywhere"
      },
      {
        "name": "Guerrilla Mail",
        "description": "Disposable email"
      }
    ],
    "DNS & Subdomains": [
      {
        "name": "Amass",
        "description": "Subdomain enum & recon",
        "integrable": true,
        "entity_types": [
          "domain"
        ],
        "keyless": true
      },
      {
        "name": "findsubdomains",
        "description": "Passive subdomain discovery",
        "integrable": true,
        "entity_types": [
          "domain"
        ],
        "keyless": false
      },
      {
        "name": "Merklemap",
        "description": "Subdomains via CT logs",
        "integrable": true,
        "entity_types": [
          "domain"
        ],
        "keyless": false
      },
      {
        "name": "Columbus Project",
        "description": "Fast subdomain API",
        "integrable": true,
        "entity_types": [
          "domain"
        ],
        "keyless": false
      },
      {
        "name": "DNSservices",
        "description": "Embedded services in DNS",
        "integrable": true,
        "entity_types": [
          "domain"
        ],
        "keyless": true
      }
    ],
    "Maritime": [
      {
        "name": "VesselFinder",
        "description": "Live AIS ship tracking",
        "integrable": true,
        "entity_types": [
          "maritime"
        ],
        "keyless": false,
        "url": "https://www.vesselfinder.com/"
      }
    ],
    "OSINT Frameworks & Suites": [
      {
        "name": "Maltego",
        "description": "Graphical link-analysis platform",
        "integrable": true,
        "entity_types": [
          "domain",
          "ip",
          "email",
          "person"
        ],
        "keyless": false
      },
      {
        "name": "SpiderFoot",
        "description": "200+ module OSINT automation",
        "integrable": true,
        "entity_types": [
          "domain",
          "ip",
          "email",
          "username"
        ],
        "keyless": false
      },
      {
        "name": "theHarvester",
        "description": "Emails/subdomains/hosts",
        "integrable": true,
        "entity_types": [
          "domain"
        ],
        "keyless": true
      },
      {
        "name": "recon-ng style: Datasploit",
        "description": "Username/email/domain OSINT",
        "integrable": true,
        "entity_types": [
          "username",
          "email",
          "domain"
        ],
        "keyless": false
      },
      {
        "name": "Photon",
        "description": "OSINT web crawler",
        "integrable": true,
        "entity_types": [
          "domain",
          "url"
        ],
        "keyless": true
      },
      {
        "name": "LinkScope",
        "description": "OSINT link-analysis tool",
        "integrable": true,
        "entity_types": [
          "domain",
          "email"
        ],
        "keyless": false
      },
      {
        "name": "sn0int",
        "description": "Semi-automatic OSINT framework",
        "integrable": true,
        "entity_types": [
          "domain",
          "ip"
        ],
        "keyless": false
      },
      {
        "name": "Sub3 Suite"
      },
      {
        "name": "SpiderSuite"
      },
      {
        "name": "Sintelix"
      },
      {
        "name": "Intrigue Core",
        "description": "Attack-surface discovery",
        "integrable": true,
        "entity_types": [
          "domain"
        ],
        "keyless": false
      },
      {
        "name": "Belati"
      },
      {
        "name": "OSINT.SH",
        "description": "Info-gathering toolset"
      },
      {
        "name": "Orbit",
        "description": "Map crypto wallet relationships",
        "integrable": true,
        "entity_types": [
          "wallet"
        ],
        "keyless": false
      },
      {
        "name": "Hunchly",
        "description": "Investigation web-capture"
      },
      {
        "name": "OSINT Framework",
        "description": "Web directory of OSINT tools",
        "url": "https://osintframework.com/"
      },
      {
        "name": "OSINT-Tool",
        "description": "Browser extension utility suite"
      },
      {
        "name": "BBOT",
        "description": "Automated recursive recon & OSINT framework",
        "url": "https://github.com/blacklanternsecurity/bbot",
        "integrable": true,
        "entity_types": [
          "domain",
          "ip",
          "email"
        ],
        "keyless": true
      }
    ],
    "Threat Intelligence": [
      {
        "name": "OTX AlienVault",
        "description": "Open Threat Exchange pulses",
        "integrable": true,
        "entity_types": [
          "ip",
          "domain",
          "hash"
        ],
        "keyless": false
      },
      {
        "name": "GreyNoise",
        "description": "Internet background-noise intel",
        "integrable": true,
        "entity_types": [
          "ip"
        ],
        "keyless": false
      },
      {
        "name": "CyberGordon",
        "description": "Multi-source IoC search",
        "integrable": true,
        "entity_types": [
          "ip",
          "domain",
          "hash"
        ],
        "keyless": false
      },
      {
        "name": "Cyberbro",
        "description": "Self-hosted IoC reputation",
        "integrable": true,
        "entity_types": [
          "ip",
          "domain",
          "hash"
        ],
        "keyless": true
      },
      {
        "name": "GitGuardian",
        "description": "Public GitHub secret monitoring",
        "integrable": true,
        "entity_types": [
          "domain"
        ],
        "keyless": false
      },
      {
        "name": "OnionScan",
        "description": "Dark-web site investigation"
      },
      {
        "name": "onion-lookup",
        "description": "Check .onion existence/metadata"
      },
      {
        "name": "REScure",
        "description": "Independent threat-intel feed",
        "integrable": true,
        "entity_types": [
          "ip",
          "domain"
        ],
        "keyless": true
      },
      {
        "name": "CrowdSec",
        "description": "Collaborative IPS/IDS"
      },
      {
        "name": "OpenCTI",
        "description": "Cyber-threat-intelligence management platform (Filigran)",
        "url": "https://filigran.io/platform/opencti/"
      },
      {
        "name": "Kaspersky Cyberthreat Map",
        "description": "Global visualization of live cyber attacks",
        "url": "https://cybermap.kaspersky.com/"
      }
    ],
    "Blogs & Communities": [
      {
        "name": "Bellingcat"
      },
      {
        "name": "IntelTechniques"
      },
      {
        "name": "OSINTCurious"
      },
      {
        "name": "NixIntel"
      },
      {
        "name": "Sector035 (Week in OSINT)"
      },
      {
        "name": "OSINT Dojo"
      },
      {
        "name": "OSINT Ambition"
      },
      {
        "name": "OSINT Team"
      }
    ],
    "Aircraft & Vessel Tracking": [
      {
        "name": "Airplanes.live",
        "description": "Live ADS-B aircraft tracking & feed",
        "url": "https://airplanes.live/",
        "integrable": true,
        "entity_types": [
          "aircraft"
        ],
        "keyless": true
      },
      {
        "name": "MarineTraffic",
        "description": "Vessel tracking & maritime intelligence",
        "url": "https://www.marinetraffic.com/",
        "integrable": true,
        "entity_types": [
          "maritime"
        ],
        "keyless": false
      },
      {
        "name": "BirdHunt (HuntIntel)",
        "description": "Tracking & intelligence research tool",
        "url": "https://birdhunt.huntintel.io/"
      }
    ],
    "Start Pages & Directories": [
      {
        "name": "OSINT4ALL (start.me)",
        "description": "Curated OSINT resource start page",
        "url": "https://start.me/p/L1rEYQ/osint4all"
      },
      {
        "name": "Awesome OSINT",
        "description": "Community-maintained OSINT resource list",
        "url": "https://github.com/jivoi/awesome-osint"
      },
      {
        "name": "Scalytics OSINT Tools",
        "description": "OSINT tools & investigation resources",
        "url": "https://osint.scalytics.io/"
      },
      {
        "name": "Pavindas OSINT Collection",
        "description": "OSINT resource directory",
        "url": "https://pavindas.github.io/osint/"
      },
      {
        "name": "ROSINT",
        "description": "OSINT resources & tools collection",
        "url": "https://www.rosint.dev/"
      },
      {
        "name": "OpenArchive",
        "description": "OSINT archive & research resource",
        "url": "https://openarchive.lol/"
      },
      {
        "name": "OSINT Newsletter — Phone Tools",
        "description": "Phone-number OSINT tool directory",
        "url": "https://tools.osintnewsletter.com/tool-categories/phone-number-osint"
      },
      {
        "name": "OSINT Industries — Phone Guide",
        "description": "How-to guide for phone-number investigations",
        "url": "https://www.osint.industries/"
      }
    ],
    "Offensive / Phishing Research (authorized only)": [
      {
        "name": "Trape",
        "description": "People-tracking & social-engineering research framework",
        "url": "https://github.com/jofpin/trape",
        "caution": "Generates tracking links to deanonymize targets. Authorized red-team / research use only — not wired into the platform."
      }
    ]
  }
}