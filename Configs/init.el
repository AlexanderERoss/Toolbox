;; init.el --- Emacs configuration

;; INSTALL PACKAGES
;; --------------------------------------------------

(require 'package)

(add-to-list 'package-archives
	     '("melpa-stable" . "https://stable.melpa.org/packages/") t)

(package-initialize)

(when (not package-archive-contents)
  (package-refresh-contents))

;; List of packages downloaded here

(defvar myPackages
  '(;; better-defaults ;; Sets better defaults such as clipboard from X and no GUI menu
    flycheck ;; Spell check
    material-theme ;; The dark material theme developed by Google
    elpy ;; Adds the Python Integration Package (elpy)
    web-mode ;; Integration for HTML, CSS, and JS
    ))

(mapc #'(lambda (package)
    (unless (package-installed-p package)
      (package-install package)))
      myPackages)

  ;; Custom downloaded path (normally as above in comment...)
(add-to-list 'load-path "~/.emacs.d/load-files/better-defaults")
(require 'better-defaults)

;; SERVER START - Starts emacsclient to use emacs internally
;; --------------------------------------------------
;; Also need to add the following to .bashrc file
;; export EDITOR="emacsclient"

(server-start)

;; THEMES
;; --------------------------------------------------
(load-theme 'material t) ;; load material theme

;; set transparency
(set-frame-parameter (selected-frame) 'alpha '(95 95))
(add-to-list 'default-frame-alist '(alpha 95 95))

;; GENERAL CUSTOMISATION
;; -------------------------------------------------

;; (setq inhibit-startup-message t) ;; hide the startup message
(global-linum-mode t) ;; enable line numbers globally
;; (pc-selection-mode) ;;Allows the Cut (C-DEL), Copy (C-INS), and Paste (S-INS) from clipboard (for Windows)

;; PACKAGE CUSTOMISATION
;; --------------------------------------------------

;; C Configuration

(global-set-key [f4] 'compile)

;; AucTex Configuration

(setq latex-run-command "pdflatex")

;; Elpy
(elpy-enable)

;; Auto-Complete


;; Web Mode
(require 'web-mode)

(add-to-list 'auto-mode-alist '("\\.html?\\'" . web-mode))

(add-to-list 'auto-mode-alist '("\\.phtml\\'" . web-mode))
(add-to-list 'auto-mode-alist '("\\.tpl\\.php\\'" . web-mode))
(add-to-list 'auto-mode-alist '("\\.[agj]sp\\'" . web-mode))
(add-to-list 'auto-mode-alist '("\\.as[cp]x\\'" . web-mode))
(add-to-list 'auto-mode-alist '("\\.erb\\'" . web-mode))
(add-to-list 'auto-mode-alist '("\\.mustache\\'" . web-mode))
(add-to-list 'auto-mode-alist '("\\.djhtml\\'" . web-mode))

;; --------------------------------------------------
;; init.el ends here
(custom-set-variables
 ;; custom-set-variables was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
 '(package-selected-packages (quote (web-mode elpy material-theme flycheck))))
(custom-set-faces
 ;; custom-set-faces was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
 )
