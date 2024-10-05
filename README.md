# mac-env
### my macbook's system preferences and environment setup and configuration


2참고: https://subicura.com/mac/dev/#디자인-설정

iTerm2를 실행하고 설정(⌘ + ,)창에서 Profiles 항목을 선택하고 Colors탭을 선택.

snazzy theme download link: 
https://subicura.com/mac/files/Snazzy.itermcolors

마진 수정
iTerm Regular Theme iTerm Minimal Theme

Apperance > Panes > Side margins: 5 -> 12
Apperance > Panes > Top & bottom margins: 2 -> 10
#




## this is to setup the initial system preference and environment setup and configuration.

first to set up home brew:

open the terminal, and execute the below script to configure almost all settings in system preferences and finder configuration.
/bin/zsh -c "$(curl -fsSL https://raw.githubusercontent.com/subicura/settings/main/macos/system_setting.zsh)"

after executing above, you must restart the mac to relfect the changes you made. you can check the detail in the below address:
https://github.com/subicura/settings/blob/main/macos/system_setting.zsh

kor)
자동 설정 스크립트
macOS는 각종 설정을 보통 ~/Library/Preferences 폴더에 .plist 파일로 관리합니다. 시스템 및 파인더 설정도 동일한 방식을 사용하고 defaults 명령어로 설정할 수 있기 때문에 스크립트로 자동화 할 수 있습니다.

additional modification
unfortunately, you cannot customize all the setups you want through the above autoscript.
you must do the below three items by youself

system preferences - language and region
https://subicura.com/mac/setup/#언어-및-지역-language-region
keyboard > text: turn off all the auto-correction 
language & region 

system preferences - security
finder preferences - download folder option 


### basic application list
1. brew install
    a. brew install --cask google-chrome
    b. brew install --cask naver-whale
    c. brew install --cask firefox
    d. brew install --cask iterm2 
        #### iterm2 설정은 별도 문서 참고
    e. brew install --cask slack
    f. brew install --cask typora
    g. brew install --cask evernote
    h. brew install --cask notion
    i. brew install --cask telegram 

2. mas  
    a. kakaotalk
    b. runcat
        mas install 1429033973
3.  
4.  
5. magnet: direct download
6. 

# brew dump file list
$ cat Brewfile
james@Jamess-MacBook-Pro ~ % cat brewfile
tap "homebrew/bundle"
tap "homebrew/cask"
tap "homebrew/cask-fonts"
tap "homebrew/core"
brew "archey"
brew "asdf"
brew "bat"
brew "cask"
brew "fasd"
brew "fzf"
brew "git"
brew "git-lfs"
brew "gnupg"
brew "htop"
brew "jq"
brew "neofetch"
brew "neovim"
brew "python@3.9"
brew "node"
brew "speedtest-cli"
brew "youtube-dl"
cask "1password"
cask "appcleaner"
cask "bartender"
cask "dbeaver-community"
cask "discord"
cask "docker"
cask "dozer"
cask "eul"
cask "firefox"
cask "font-meslo-lg-nerd-font"
cask "iina"
cask "itsycal"
cask "karabiner-elements"
cask "keka"
cask "maccy"
cask "microsoft-auto-update"
cask "miro"
cask "openinterminal-lite"
cask "powershell"
cask "rectangle"
cask "sequel-pro"
cask "termius"
cask "visual-studio-code"
james@Jamess-MacBook-Pro ~ %

# 출력 내용
tap "caskroom/fonts"
tap "cjbassi/gotop"
tap "dart-lang/dart"
tap "getsentry/tools"
tap "homebrew/bundle"
tap "homebrew/cask"
tap "homebrew/cask-drivers"
tap "homebrew/cask-fonts"
tap "homebrew/cask-versions"
tap "homebrew/core"
tap "vitorgalvao/tinybashs"
brew "autojump"
brew "awscli"
brew "bat"
brew "git-flow-avh"
brew "mysql"
brew "mysql@5.7"
brew "zsh-autosuggestions"
brew "zsh-syntax-highlighting"
brew "dart-lang/dart/dart"
brew "vitorgalvao/tinybashs/cask-repair"
cask "alacritty"
cask "font-hack-nerd-font"

## 다른 맥에서 입력
$ brew bundle


## mas에서 wechat 검색
mas search wechat

### 출력
836500024      WeChat            (2.3.28)
1189898970    WeChat Work     (2.8.16)

#WeChat의 id는 836500024

#brewfile리스트에는 다음 문구를 추가하면 된다.
mas "WeChat", 836500024

## rosetta 2 installation
softwareupdate --install-rosetta --agree-to-license

#git
##설정
git lfs install
git config --global user.name "greathedgehog"
git config --global user.email "jamesbjoy7@gmail.com"
git config --global core.precomposeunicode true
git config --global core.quotepath false

main manual:
https://subicura.com/mac/setup/setting.html#스크립트-실행

for reference:
https://blog.gangnamunni.com/post/brew_cask_mas/



내가 설치한 맥용 애플리케이션들
https://youngmind.tistory.com/entry/내가-설치한-맥용-어플리케이션들
 
한방에 설치하기 (위챗 포함)
https://npd-58.tistory.com/5

to setup team development environment using brewfile 
https://velog.io/@iamchanii/Brewfile을-이용해서-팀-개발-환경-만들기


## About Me
Hello! I'm interested in finance, IT, and fitness. My GitHub is a collection of projects and learning resources focusing on web development, AI, machine learning, and financial technology. I aim to share my journey through consistent learning, project building, and content creation. 

## 🔥 Current Focus
- **Web Development**: Projects using Python (Flask/Django) and JavaScript (React/Node.js)
- **AI & Machine Learning**: Exploring AI projects and participating in Kaggle competitions
- **Finance & Investment**: Developing financial tools and analysis for stock portfolio management
- **Health & Fitness**: Documenting my marathon and fitness journey while working on my VO2 max and strength training goals

## 📁 Repository Categories

### 1. Work
- **HRD Projects**: Internal education and training materials related to HR development.
- **Financial IT**: Projects focused on financial cloud services and system development.
- **Projects**: Progress on various development projects, including web and AI.

### 2. Personal Development
- **IT Learning**: Resources and code projects related to Python, JavaScript, and AI/ML.
  - [Python Projects](#)
  - [JavaScript Projects](#)
  - [Machine Learning Projects](#)
- **Investment Management**: Tools and scripts for tracking my investment portfolio and financial goals.

### 3. Health & Fitness
- **Workout Plans**: My workout schedules for strength training, running, and swimming.
- **Fitness Analytics**: Scripts to analyze workout performance using data from Garmin, Apple Watch, and Planfit.

### 4. Creative & Blog
- **GitHub Blog**: My personal blog with articles about web development, AI, and investment.
  - [Latest Blog Post](#)
- **YouTube**: Planning and content for my YouTube channel where I share tutorials, financial analysis, and tech insights.
- **Writing Projects**: Ideas and drafts for future book publications.

## 🌱 Ongoing Projects
- **[Stock Prediction Dashboard](#)**: A stock scoring system based on technical indicators for buy/sell decisions.
- **[QR Code Attendance System](#)**: A web-based attendance system using QR codes.

## 🚀 How to Navigate
1. **Explore the repositories**: Browse through different categories of my work.
2. **Follow my learning journey**: Check out my learning projects in Python and AI.
3. **Engage with my content**: Follow my blog and YouTube for more insights on finance and technology.

## 🛠️ Tools & Technologies
- **Languages**: Python, JavaScript (React, Node.js), HTML, CSS
- **Frameworks**: Flask, Django, TensorFlow, PyTorch
- **Tools**: Git, VSCode, Google Colab, Figma
- **Cloud Services**: Google Cloud

## 📝 Contact
- **Email**: [jamesbjoy7@gmail.com](mailto:jamesbjoy7@gmail.com)
- **LinkedIn**: [Your LinkedIn](https://www.linkedin.com/in/your-profile/)
- **YouTube**: [Your YouTube Channel](https://www.youtube.com/channel/your-channel)

Thank you for visiting my GitHub! Feel free to explore and contribute to any projects that interest you.
