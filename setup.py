{"payload":{"allShortcutsEnabled":true,"fileTree":{"":{"items":[{"name":".devcontainer","path":".devcontainer","contentType":"directory"},{"name":".github","path":".github","contentType":"directory"},{"name":"docs","path":"docs","contentType":"directory"},{"name":"docsrc","path":"docsrc","contentType":"directory"},{"name":"examples","path":"examples","contentType":"directory"},{"name":"src","path":"src","contentType":"directory"},{"name":"tests","path":"tests","contentType":"directory"},{"name":"venv","path":"venv","contentType":"directory"},{"name":".gitignore","path":".gitignore","contentType":"file"},{"name":".pre-commit-config.yaml","path":".pre-commit-config.yaml","contentType":"file"},{"name":".releaserc.json","path":".releaserc.json","contentType":"file"},{"name":"CONTRIBUTING.md","path":"CONTRIBUTING.md","contentType":"file"},{"name":"LICENSE","path":"LICENSE","contentType":"file"},{"name":"MANIFEST.in","path":"MANIFEST.in","contentType":"file"},{"name":"Makefile","path":"Makefile","contentType":"file"},{"name":"README.md","path":"README.md","contentType":"file"},{"name":"commitlint.config.js","path":"commitlint.config.js","contentType":"file"},{"name":"make.bat","path":"make.bat","contentType":"file"},{"name":"mkdocs.yml","path":"mkdocs.yml","contentType":"file"},{"name":"renovate.json","path":"renovate.json","contentType":"file"},{"name":"requirements-dev.txt","path":"requirements-dev.txt","contentType":"file"},{"name":"requirements-docs.txt","path":"requirements-docs.txt","contentType":"file"},{"name":"requirements-spark.txt","path":"requirements-spark.txt","contentType":"file"},{"name":"requirements-test.txt","path":"requirements-test.txt","contentType":"file"},{"name":"requirements.txt","path":"requirements.txt","contentType":"file"},{"name":"setup.py","path":"setup.py","contentType":"file"}],"totalCount":26}},"fileTreeProcessingTime":3.7874689999999998,"foldersToFetch":[],"reducedMotionEnabled":"system","repo":{"id":49346299,"defaultBranch":"develop","name":"ydata-profiling","ownerLogin":"ydataai","currentUserCanPush":false,"isFork":false,"isEmpty":false,"createdAt":"2016-01-09T21:47:55.000-02:00","ownerAvatar":"https://avatars.githubusercontent.com/u/57689451?v=4","public":true,"private":false,"isOrgOwned":true},"symbolsExpanded":false,"treeExpanded":true,"refInfo":{"name":"develop","listCacheKey":"v0:1701229768.0","canEdit":true,"refType":"branch","currentOid":"9cecfbd61212348aaea16f439c423b7513a0902b"},"path":"setup.py","currentUser":{"id":108198403,"login":"FabioPojo1987","userEmail":"fabio_pojo@hotmail.com"},"blob":{"rawLines":["from pathlib import Path","","from setuptools import find_packages, setup","","# Read the contents of README file","source_root = Path(\".\")","with (source_root / \"README.md\").open(encoding=\"utf-8\") as f:","    long_description = f.read()","","# Read the requirements","with (source_root / \"requirements.txt\").open(encoding=\"utf8\") as f:","    requirements = f.readlines()","","try:","    version = (source_root / \"VERSION\").read_text().rstrip(\"\\n\")","except FileNotFoundError:","    version = \"0.0.dev0\"","","with open(source_root / \"src/ydata_profiling/version.py\", \"w\") as version_file:","    version_file.write(f\"__version__ = '{version}'\")","","setup(","    name=\"ydata-profiling\",","    version=version,","    author=\"YData Labs Inc\",","    author_email=\"opensource@ydata.ai\",","    packages=find_packages(\"src\"),","    package_dir={\"\": \"src\"},","    url=\"https://github.com/ydataai/ydata-profiling\",","    license=\"MIT\",","    description=\"Generate profile report for pandas DataFrame\",","    python_requires=\">=3.7, <3.12\",","    install_requires=requirements,","    extras_require={","        \"notebook\": [","            \"jupyter-client>=5.3.4\",","            \"jupyter-core>=4.6.3\",","            \"ipywidgets>=7.5.1\",","        ],","        \"unicode\": [","            \"tangled-up-in-unicode==0.2.0\",","        ],","    },","    package_data={","        \"ydata_profiling\": [\"py.typed\"],","    },","    include_package_data=True,","    classifiers=[","        \"Development Status :: 5 - Production/Stable\",","        \"Topic :: Software Development :: Build Tools\",","        \"License :: OSI Approved :: MIT License\",","        \"Environment :: Console\",","        \"Operating System :: OS Independent\",","        \"Intended Audience :: Science/Research\",","        \"Intended Audience :: Developers\",","        \"Intended Audience :: Financial and Insurance Industry\",","        \"Intended Audience :: Healthcare Industry\",","        \"Topic :: Scientific/Engineering\",","        \"Framework :: IPython\",","        \"Programming Language :: Python :: 3\",","        \"Programming Language :: Python :: 3.7\",","        \"Programming Language :: Python :: 3.8\",","        \"Programming Language :: Python :: 3.9\",","        \"Programming Language :: Python :: 3.10\",","        \"Programming Language :: Python :: 3.11\",","    ],","    keywords=\"pandas data-science data-analysis python jupyter ipython\",","    long_description=long_description,","    long_description_content_type=\"text/markdown\",","    entry_points={","        \"console_scripts\": [","            \"ydata_profiling = ydata_profiling.controller.console:main\",","            \"pandas_profiling = ydata_profiling.controller.console:main\",","        ]","    },","    options={\"bdist_wheel\": {\"universal\": True}},",")"],"stylingDirectives":[[{"start":0,"end":4,"cssClass":"pl-k"},{"start":5,"end":12,"cssClass":"pl-s1"},{"start":13,"end":19,"cssClass":"pl-k"},{"start":20,"end":24,"cssClass":"pl-v"}],[],[{"start":0,"end":4,"cssClass":"pl-k"},{"start":5,"end":15,"cssClass":"pl-s1"},{"start":16,"end":22,"cssClass":"pl-k"},{"start":23,"end":36,"cssClass":"pl-s1"},{"start":38,"end":43,"cssClass":"pl-s1"}],[],[{"start":0,"end":34,"cssClass":"pl-c"}],[{"start":0,"end":11,"cssClass":"pl-s1"},{"start":12,"end":13,"cssClass":"pl-c1"},{"start":14,"end":18,"cssClass":"pl-v"},{"start":19,"end":22,"cssClass":"pl-s"}],[{"start":0,"end":4,"cssClass":"pl-k"},{"start":6,"end":17,"cssClass":"pl-s1"},{"start":18,"end":19,"cssClass":"pl-c1"},{"start":20,"end":31,"cssClass":"pl-s"},{"start":33,"end":37,"cssClass":"pl-en"},{"start":38,"end":46,"cssClass":"pl-s1"},{"start":46,"end":47,"cssClass":"pl-c1"},{"start":47,"end":54,"cssClass":"pl-s"},{"start":56,"end":58,"cssClass":"pl-k"},{"start":59,"end":60,"cssClass":"pl-s1"}],[{"start":4,"end":20,"cssClass":"pl-s1"},{"start":21,"end":22,"cssClass":"pl-c1"},{"start":23,"end":24,"cssClass":"pl-s1"},{"start":25,"end":29,"cssClass":"pl-en"}],[],[{"start":0,"end":23,"cssClass":"pl-c"}],[{"start":0,"end":4,"cssClass":"pl-k"},{"start":6,"end":17,"cssClass":"pl-s1"},{"start":18,"end":19,"cssClass":"pl-c1"},{"start":20,"end":38,"cssClass":"pl-s"},{"start":40,"end":44,"cssClass":"pl-en"},{"start":45,"end":53,"cssClass":"pl-s1"},{"start":53,"end":54,"cssClass":"pl-c1"},{"start":54,"end":60,"cssClass":"pl-s"},{"start":62,"end":64,"cssClass":"pl-k"},{"start":65,"end":66,"cssClass":"pl-s1"}],[{"start":4,"end":16,"cssClass":"pl-s1"},{"start":17,"end":18,"cssClass":"pl-c1"},{"start":19,"end":20,"cssClass":"pl-s1"},{"start":21,"end":30,"cssClass":"pl-en"}],[],[{"start":0,"end":3,"cssClass":"pl-k"}],[{"start":4,"end":11,"cssClass":"pl-s1"},{"start":12,"end":13,"cssClass":"pl-c1"},{"start":15,"end":26,"cssClass":"pl-s1"},{"start":27,"end":28,"cssClass":"pl-c1"},{"start":29,"end":38,"cssClass":"pl-s"},{"start":40,"end":49,"cssClass":"pl-en"},{"start":52,"end":58,"cssClass":"pl-en"},{"start":59,"end":63,"cssClass":"pl-s"},{"start":60,"end":62,"cssClass":"pl-cce"}],[{"start":0,"end":6,"cssClass":"pl-k"},{"start":7,"end":24,"cssClass":"pl-v"}],[{"start":4,"end":11,"cssClass":"pl-s1"},{"start":12,"end":13,"cssClass":"pl-c1"},{"start":14,"end":24,"cssClass":"pl-s"}],[],[{"start":0,"end":4,"cssClass":"pl-k"},{"start":5,"end":9,"cssClass":"pl-en"},{"start":10,"end":21,"cssClass":"pl-s1"},{"start":22,"end":23,"cssClass":"pl-c1"},{"start":24,"end":56,"cssClass":"pl-s"},{"start":58,"end":61,"cssClass":"pl-s"},{"start":63,"end":65,"cssClass":"pl-k"},{"start":66,"end":78,"cssClass":"pl-s1"}],[{"start":4,"end":16,"cssClass":"pl-s1"},{"start":17,"end":22,"cssClass":"pl-en"},{"start":23,"end":51,"cssClass":"pl-s"},{"start":40,"end":49,"cssClass":"pl-s1"},{"start":40,"end":41,"cssClass":"pl-kos"},{"start":41,"end":48,"cssClass":"pl-s1"},{"start":48,"end":49,"cssClass":"pl-kos"}],[],[{"start":0,"end":5,"cssClass":"pl-en"}],[{"start":4,"end":8,"cssClass":"pl-s1"},{"start":8,"end":9,"cssClass":"pl-c1"},{"start":9,"end":26,"cssClass":"pl-s"}],[{"start":4,"end":11,"cssClass":"pl-s1"},{"start":11,"end":12,"cssClass":"pl-c1"},{"start":12,"end":19,"cssClass":"pl-s1"}],[{"start":4,"end":10,"cssClass":"pl-s1"},{"start":10,"end":11,"cssClass":"pl-c1"},{"start":11,"end":27,"cssClass":"pl-s"}],[{"start":4,"end":16,"cssClass":"pl-s1"},{"start":16,"end":17,"cssClass":"pl-c1"},{"start":17,"end":38,"cssClass":"pl-s"}],[{"start":4,"end":12,"cssClass":"pl-s1"},{"start":12,"end":13,"cssClass":"pl-c1"},{"start":13,"end":26,"cssClass":"pl-en"},{"start":27,"end":32,"cssClass":"pl-s"}],[{"start":4,"end":15,"cssClass":"pl-s1"},{"start":15,"end":16,"cssClass":"pl-c1"},{"start":17,"end":19,"cssClass":"pl-s"},{"start":21,"end":26,"cssClass":"pl-s"}],[{"start":4,"end":7,"cssClass":"pl-s1"},{"start":7,"end":8,"cssClass":"pl-c1"},{"start":8,"end":52,"cssClass":"pl-s"}],[{"start":4,"end":11,"cssClass":"pl-s1"},{"start":11,"end":12,"cssClass":"pl-c1"},{"start":12,"end":17,"cssClass":"pl-s"}],[{"start":4,"end":15,"cssClass":"pl-s1"},{"start":15,"end":16,"cssClass":"pl-c1"},{"start":16,"end":62,"cssClass":"pl-s"}],[{"start":4,"end":19,"cssClass":"pl-s1"},{"start":19,"end":20,"cssClass":"pl-c1"},{"start":20,"end":34,"cssClass":"pl-s"}],[{"start":4,"end":20,"cssClass":"pl-s1"},{"start":20,"end":21,"cssClass":"pl-c1"},{"start":21,"end":33,"cssClass":"pl-s1"}],[{"start":4,"end":18,"cssClass":"pl-s1"},{"start":18,"end":19,"cssClass":"pl-c1"}],[{"start":8,"end":18,"cssClass":"pl-s"}],[{"start":12,"end":35,"cssClass":"pl-s"}],[{"start":12,"end":33,"cssClass":"pl-s"}],[{"start":12,"end":31,"cssClass":"pl-s"}],[],[{"start":8,"end":17,"cssClass":"pl-s"}],[{"start":12,"end":42,"cssClass":"pl-s"}],[],[],[{"start":4,"end":16,"cssClass":"pl-s1"},{"start":16,"end":17,"cssClass":"pl-c1"}],[{"start":8,"end":25,"cssClass":"pl-s"},{"start":28,"end":38,"cssClass":"pl-s"}],[],[{"start":4,"end":24,"cssClass":"pl-s1"},{"start":24,"end":25,"cssClass":"pl-c1"},{"start":25,"end":29,"cssClass":"pl-c1"}],[{"start":4,"end":15,"cssClass":"pl-s1"},{"start":15,"end":16,"cssClass":"pl-c1"}],[{"start":8,"end":53,"cssClass":"pl-s"}],[{"start":8,"end":54,"cssClass":"pl-s"}],[{"start":8,"end":48,"cssClass":"pl-s"}],[{"start":8,"end":32,"cssClass":"pl-s"}],[{"start":8,"end":44,"cssClass":"pl-s"}],[{"start":8,"end":47,"cssClass":"pl-s"}],[{"start":8,"end":41,"cssClass":"pl-s"}],[{"start":8,"end":63,"cssClass":"pl-s"}],[{"start":8,"end":50,"cssClass":"pl-s"}],[{"start":8,"end":41,"cssClass":"pl-s"}],[{"start":8,"end":30,"cssClass":"pl-s"}],[{"start":8,"end":45,"cssClass":"pl-s"}],[{"start":8,"end":47,"cssClass":"pl-s"}],[{"start":8,"end":47,"cssClass":"pl-s"}],[{"start":8,"end":47,"cssClass":"pl-s"}],[{"start":8,"end":48,"cssClass":"pl-s"}],[{"start":8,"end":48,"cssClass":"pl-s"}],[],[{"start":4,"end":12,"cssClass":"pl-s1"},{"start":12,"end":13,"cssClass":"pl-c1"},{"start":13,"end":71,"cssClass":"pl-s"}],[{"start":4,"end":20,"cssClass":"pl-s1"},{"start":20,"end":21,"cssClass":"pl-c1"},{"start":21,"end":37,"cssClass":"pl-s1"}],[{"start":4,"end":33,"cssClass":"pl-s1"},{"start":33,"end":34,"cssClass":"pl-c1"},{"start":34,"end":49,"cssClass":"pl-s"}],[{"start":4,"end":16,"cssClass":"pl-s1"},{"start":16,"end":17,"cssClass":"pl-c1"}],[{"start":8,"end":25,"cssClass":"pl-s"}],[{"start":12,"end":71,"cssClass":"pl-s"}],[{"start":12,"end":72,"cssClass":"pl-s"}],[],[],[{"start":4,"end":11,"cssClass":"pl-s1"},{"start":11,"end":12,"cssClass":"pl-c1"},{"start":13,"end":26,"cssClass":"pl-s"},{"start":29,"end":40,"cssClass":"pl-s"},{"start":42,"end":46,"cssClass":"pl-c1"}],[]],"csv":null,"csvError":null,"dependabotInfo":{"showConfigurationBanner":false,"configFilePath":null,"networkDependabotPath":"/ydataai/ydata-profiling/network/updates","dismissConfigurationNoticePath":"/settings/dismiss-notice/dependabot_configuration_notice","configurationNoticeDismissed":false,"repoAlertsPath":"/ydataai/ydata-profiling/security/dependabot","repoSecurityAndAnalysisPath":"/ydataai/ydata-profiling/settings/security_analysis","repoOwnerIsOrg":true,"currentUserCanAdminRepo":false},"displayName":"setup.py","displayUrl":"https://github.com/ydataai/ydata-profiling/blob/develop/setup.py?raw=true","headerInfo":{"blobSize":"2.55 KB","deleteInfo":{"deleteTooltip":"Fork this repository and delete the file"},"editInfo":{"editTooltip":"Fork this repository and edit the file"},"ghDesktopPath":"https://desktop.github.com","gitLfsPath":null,"onBranch":true,"shortPath":"85dd2e1","siteNavLoginPath":"/login?return_to=https%3A%2F%2Fgithub.com%2Fydataai%2Fydata-profiling%2Fblob%2Fdevelop%2Fsetup.py","isCSV":false,"isRichtext":false,"toc":null,"lineInfo":{"truncatedLoc":"77","truncatedSloc":"71"},"mode":"file"},"image":false,"isCodeownersFile":null,"isPlain":false,"isValidLegacyIssueTemplate":false,"issueTemplateHelpUrl":"https://docs.github.com/articles/about-issue-and-pull-request-templates","issueTemplate":null,"discussionTemplate":null,"language":"Python","languageID":303,"large":false,"loggedIn":true,"newDiscussionPath":"/ydataai/ydata-profiling/discussions/new","newIssuePath":"/ydataai/ydata-profiling/issues/new","planSupportInfo":{"repoIsFork":null,"repoOwnedByCurrentUser":null,"requestFullPath":"/ydataai/ydata-profiling/blob/develop/setup.py","showFreeOrgGatedFeatureMessage":null,"showPlanSupportBanner":null,"upgradeDataAttributes":null,"upgradePath":null},"publishBannersInfo":{"dismissActionNoticePath":"/settings/dismiss-notice/publish_action_from_dockerfile","dismissStackNoticePath":"/settings/dismiss-notice/publish_stack_from_file","releasePath":"/ydataai/ydata-profiling/releases/new?marketplace=true","showPublishActionBanner":false,"showPublishStackBanner":false},"rawBlobUrl":"https://github.com/ydataai/ydata-profiling/raw/develop/setup.py","renderImageOrRaw":false,"richText":null,"renderedFileInfo":null,"shortPath":null,"tabSize":8,"topBannersInfo":{"overridingGlobalFundingFile":false,"globalPreferredFundingPath":null,"repoOwner":"ydataai","repoName":"ydata-profiling","showInvalidCitationWarning":false,"citationHelpUrl":"https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/creating-a-repository-on-github/about-citation-files","showDependabotConfigurationBanner":false,"actionsOnboardingTip":null},"truncated":false,"viewable":true,"workflowRedirectUrl":null,"symbols":{"timedOut":false,"notAnalyzed":false,"symbols":[{"name":"source_root","kind":"constant","identStart":106,"identEnd":117,"extentStart":106,"extentEnd":129,"fullyQualifiedName":"source_root","identUtf16":{"start":{"lineNumber":5,"utf16Col":0},"end":{"lineNumber":5,"utf16Col":11}},"extentUtf16":{"start":{"lineNumber":5,"utf16Col":0},"end":{"lineNumber":5,"utf16Col":23}}}]}},"copilotInfo":null,"copilotAccessAllowed":false,"csrf_tokens":{"/ydataai/ydata-profiling/branches":{"post":"Ex_PlpIcpe3__OJ9cD4IE39cTq9bmsSD7zMhk27y7J80z3_ZdNFtOlBuIcrpeRe4l_dhZGbAxpJXpISkzQYLXw"},"/repos/preferences":{"post":"FL4zBkgDGMVtoGvH-WO3wIE8NPFUNRqnYvGvt6JWixy1ou-D5razW0UbDUDUHa3EaHl3m1WYSDSwQenrchdKXQ"}}},"title":"ydata-profiling/setup.py at develop · ydataai/ydata-profiling"}