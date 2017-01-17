<?php

/* AcmeDemoBundle::layout.html.twig */
class __TwigTemplate_c59984c10ad36aa85b1d97fa29b45dc509612cd11138354d86b6055496f3f1ba extends Twig_Template
{
    public function __construct(Twig_Environment $env)
    {
        parent::__construct($env);

        $this->parent = $this->env->loadTemplate("TwigBundle::layout.html.twig");

        $this->blocks = array(
            'head' => array($this, 'block_head'),
            'title' => array($this, 'block_title'),
            'body' => array($this, 'block_body'),
            'content_header' => array($this, 'block_content_header'),
            'content_header_more' => array($this, 'block_content_header_more'),
            'content' => array($this, 'block_content'),
        );
    }

    protected function doGetParent(array $context)
    {
        return "TwigBundle::layout.html.twig";
    }

    protected function doDisplay(array $context, array $blocks = array())
    {
        $this->parent->display($context, array_merge($this->blocks, $blocks));
    }

    // line 3
    public function block_head($context, array $blocks = array())
    {
        // line 4
        echo "    <link rel=\"icon\" sizes=\"16x16\" href=\"";
        echo twig_escape_filter($this->env, $this->env->getExtension('assets')->getAssetUrl("favicon.ico"), "html", null, true);
        echo "\" />

";
    }

    // line 8
    public function block_title($context, array $blocks = array())
    {
        echo "Demo Bundle";
    }

    // line 10
    public function block_body($context, array $blocks = array())
    {
        // line 11
        echo "        ";
        $context['_parent'] = (array) $context;
        $context['_seq'] = twig_ensure_traversable($this->getAttribute($this->getAttribute($this->getAttribute((isset($context["app"]) ? $context["app"] : $this->getContext($context, "app")), "session"), "flashbag"), "get", array(0 => "notice"), "method"));
        foreach ($context['_seq'] as $context["_key"] => $context["flashMessage"]) {
            // line 12
            echo "            <div class=\"flash-message\">
                <em>Notice</em>: ";
            // line 13
            echo twig_escape_filter($this->env, (isset($context["flashMessage"]) ? $context["flashMessage"] : $this->getContext($context, "flashMessage")), "html", null, true);
            echo "

            </div>
        ";
        }
        $_parent = $context['_parent'];
        unset($context['_seq'], $context['_iterated'], $context['_key'], $context['flashMessage'], $context['_parent'], $context['loop']);
        $context = array_intersect_key($context, $_parent) + $_parent;
        // line 17
        echo "
        ";
        // line 18
        $this->displayBlock('content_header', $context, $blocks);
        // line 27
        echo "
        <div class=\"block\">
        ";
        // line 29
        $this->displayBlock('content', $context, $blocks);
        // line 30
        echo "    </div>

    ";
        // line 32
        if (array_key_exists("code", $context)) {
            // line 33
            echo "        <h2>Code behind this page</h2>
        <div class=\"block\">
            <div class=\"symfony-content\">";
            // line 35
            echo (isset($context["code"]) ? $context["code"] : $this->getContext($context, "code"));
            echo "</div>
        </div>
    ";
        }
    }

    // line 18
    public function block_content_header($context, array $blocks = array())
    {
        // line 19
        echo "            <ul id=\"menu\">
                ";
        // line 20
        $this->displayBlock('content_header_more', $context, $blocks);
        // line 23
        echo "            </ul>

            <div style=\"clear: both\"></div>
        ";
    }

    // line 20
    public function block_content_header_more($context, array $blocks = array())
    {
        // line 21
        echo "                    <li><a href=\"";
        echo $this->env->getExtension('routing')->getPath("_demo");
        echo "\">Demo Home</a></li>
                    ";
    }

    // line 29
    public function block_content($context, array $blocks = array())
    {
    }

    public function getTemplateName()
    {
        return "AcmeDemoBundle::layout.html.twig";
    }

    public function isTraitable()
    {
        return false;
    }

    public function getDebugInfo()
    {
        return array (  125 => 29,  118 => 21,  115 => 20,  108 => 23,  106 => 20,  103 => 19,  100 => 18,  92 => 35,  88 => 33,  86 => 32,  82 => 30,  80 => 29,  76 => 27,  74 => 18,  71 => 17,  61 => 13,  58 => 12,  53 => 11,  50 => 10,  44 => 8,  36 => 4,  33 => 3,);
    }
}
